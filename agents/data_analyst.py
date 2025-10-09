import pandas as pd
import numpy as np
from agents.agent_setup import get_llm, get_dataset_preview
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import io
import sys

PROMPT_TEMPLATE = """
Você é o "DataAnalystAgent", um especialista em análise de dados com PhD em Estatística. Sua tarefa é analisar o dataset fornecido e responder à pergunta do usuário de forma precisa e técnica.

**Contexto da Análise:**
{dataset_preview}

**Histórico da Conversa e Análises Anteriores:**
{analysis_context}

**Pergunta Específica para Você:**
"{specific_question}"

**Sua Resposta Deve Conter:**
1.  **Análise Direta**: Responda à pergunta com análises estatísticas detalhadas.
2.  **Métricas Relevantes**: Forneça números específicos (médias, medianas, desvios padrão, correlações, p-values, etc.).
3.  **Observações Técnicas**: Aponte padrões estatisticamente significativos, outliers (usando IQR ou Z-score), ou qualquer outra descoberta relevante.
4.  **Concisão**: Seja objetivo e foque nos dados. Não forneça conclusões de negócio, apenas os fatos analíticos.
5.  **IMPORTANTE**: Quando apresentar tabelas (como .describe(), .corr(), .value_counts()), formate-as como tabelas Markdown usando o formato:
   | Coluna 1 | Coluna 2 | Coluna 3 |
   |----------|----------|----------|
   | Valor 1  | Valor 2  | Valor 3  |

Formate sua resposta usando Markdown para clareza.
"""

def execute_statistical_code(df: pd.DataFrame, question: str):
    """
    Executa análises estatísticas comuns e retorna resultados formatados como tabelas.
    """
    results = {}
    
    try:
        # Detectar tipo de análise pela pergunta
        question_lower = question.lower()
        
        # 1. ANÁLISE DESCRITIVA (describe, estatísticas básicas)
        if any(word in question_lower for word in ['descri', 'estatística', 'resumo', 'média', 'mediana', 'desvio', 'padrão', 'mínimo', 'máximo']):
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            if len(numeric_cols) > 0:
                results['describe'] = df[numeric_cols].describe()
        
        # 2. CORRELAÇÃO
        if any(word in question_lower for word in ['correlação', 'correlacao', 'relaciona', 'influência', 'influencia']):
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            if len(numeric_cols) > 1:
                results['correlation'] = df[numeric_cols].corr()
        
        # 3. OUTLIERS (usando IQR)
        if any(word in question_lower for word in ['outlier', 'atípico', 'atipico', 'anomalia', 'anômalo']):
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            outlier_info = {}
            for col in numeric_cols:
                Q1 = df[col].quantile(0.25)
                Q3 = df[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR
                outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
                outlier_info[col] = {
                    'Total Outliers': len(outliers),
                    'Porcentagem': f"{(len(outliers)/len(df)*100):.2f}%",
                    'Limite Inferior': f"{lower_bound:.2f}",
                    'Limite Superior': f"{upper_bound:.2f}"
                }
            if outlier_info:
                results['outliers'] = pd.DataFrame(outlier_info).T
        
        # 4. VALORES MAIS FREQUENTES
        if any(word in question_lower for word in ['frequente', 'comum', 'valor_counts', 'contagem', 'distribuição']):
            # Para colunas categóricas
            cat_cols = df.select_dtypes(include=['object', 'category']).columns
            if len(cat_cols) > 0:
                freq_info = {}
                for col in cat_cols[:5]:  # Limitar a 5 colunas
                    top_5 = df[col].value_counts().head(5)
                    freq_info[col] = top_5
                if freq_info:
                    results['frequency'] = pd.DataFrame(freq_info)
        
        # 5. VALORES FALTANTES
        if any(word in question_lower for word in ['faltante', 'missing', 'nulo', 'nan', 'vazio']):
            missing_data = pd.DataFrame({
                'Total Missing': df.isnull().sum(),
                'Porcentagem': (df.isnull().sum() / len(df) * 100).round(2)
            })
            missing_data = missing_data[missing_data['Total Missing'] > 0]
            if not missing_data.empty:
                results['missing'] = missing_data
                
    except Exception as e:
        print(f"Erro ao executar análise estatística: {str(e)}")
    
    return results

def get_data_analyst_agent(api_key: str):
    llm = get_llm(api_key)
    prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    chain = prompt | llm | StrOutputParser()
    return chain

def run_data_analyst(api_key: str, df: pd.DataFrame, analysis_context: str, specific_question: str):
    try:
        # Verifica se o DataFrame está vazio
        if df.empty:
            return "Erro: O DataFrame está vazio. Não é possível realizar a análise."
            
        # Verifica se a pergunta específica foi fornecida
        if not specific_question or not specific_question.strip():
            return "Erro: Nenhuma pergunta específica foi fornecida para análise."
            
        # EXECUTAR CÓDIGO ESTATÍSTICO REAL
        statistical_results = execute_statistical_code(df, specific_question)
        
        # Formatar tabelas como markdown
        tables_markdown = ""
        if statistical_results:
            for analysis_type, result_df in statistical_results.items():
                if isinstance(result_df, pd.DataFrame):
                    tables_markdown += f"\n\n**Tabela - {analysis_type.upper()}:**\n\n"
                    tables_markdown += result_df.to_markdown() + "\n"
        
        # Obtém o agente e os dados
        agent = get_data_analyst_agent(api_key)
        dataset_preview = get_dataset_preview(df)
        
        # Adicionar contexto das tabelas geradas
        enhanced_context = f"{analysis_context}\n\nTABELAS GERADAS:\n{tables_markdown}" if tables_markdown else analysis_context
        
        # Verifica se o preview do dataset foi gerado corretamente
        if not dataset_preview:
            return "Erro: Não foi possível gerar o preview do dataset."
            
        # Executa a análise
        response = agent.invoke({
            "dataset_preview": dataset_preview,
            "analysis_context": enhanced_context or "Nenhum contexto de análise anterior fornecido.",
            "specific_question": specific_question
        })
        
        # Verifica se a resposta é válida
        if not response or response.strip() == "undefined":
            return "Desculpe, não foi possível gerar uma análise para esta pergunta. Por favor, tente reformular sua pergunta."
        
        # CONCATENAR TABELAS REAIS COM A RESPOSTA DO LLM
        final_response = response
        if tables_markdown:
            final_response = f"{response}\n\n---\n\n## TABELAS ESTATÍSTICAS GERADAS\n{tables_markdown}"
            
        return final_response
        
    except Exception as e:
        # Log do erro para depuração
        print(f"Erro no DataAnalystAgent: {str(e)}")
        return f"Ocorreu um erro ao processar sua solicitação: {str(e)}"