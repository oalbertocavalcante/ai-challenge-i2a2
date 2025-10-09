# Arquivo: agents/coordinator.py

from agents.agent_setup import get_llm, get_dataset_preview
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import json
import pandas as pd

PROMPT_TEMPLATE = """
Você é o "CoordinatorAgent", o orquestrador de um sistema de análise de dados com IA.
Sua função é receber a pergunta do usuário e decidir qual agente especializado deve ser acionado.

**Agentes Disponíveis:**
- `DataAnalystAgent`: Para perguntas que exigem análises estatísticas, números, métricas, identificação de padrões, outliers e correlações. Responde a "o quê", "quantos", "qual é a média/correlação". SEMPRE é chamado para análises descritivas, correlações, outliers, distribuições.
- `VisualizationAgent`: Para pedidos explícitos de gráficos, como "mostre um histograma", "crie um scatter plot", "gere um heatmap". TAMBÉM é chamado automaticamente após DataAnalyst para questões estatísticas (correlação, outliers, distribuição).
- `ConsultantAgent`: Para perguntas que pedem interpretação, insights de negócio, conclusões, recomendações ou o "porquê" por trás dos dados.
- `CodeGeneratorAgent`: Para pedidos explícitos de código Python, como "gere o código para esta análise", "crie um notebook Jupyter", "me dê o código para", "escreva um script Python".

**REGRA ESPECIAL - ANÁLISES ESTATÍSTICAS:**
Quando a pergunta envolver:
- Análise descritiva, estatísticas básicas, describe()
- Correlação entre variáveis
- Detecção de outliers ou anomalias
- Distribuição de dados
- Valores faltantes

Você deve retornar "BOTH" como agent_to_call, indicando que AMBOS DataAnalystAgent (tabela) E VisualizationAgent (gráfico) devem ser chamados sequencialmente.

**Contexto da Análise:**
{dataset_preview}

**Histórico da Conversa:**
{conversation_history}

**Pergunta do Usuário:**
"{user_question}"

**Sua Tarefa:**
Analise a pergunta do usuário e o contexto. Retorne um objeto JSON com a sua decisão. O JSON deve ter a seguinte estrutura:
{{
  "agent_to_call": "NOME_DO_AGENTE ou BOTH",
  "question_for_agent": "PERGUNTA_REFORMULADA_E_ESPECÍFICA_PARA_O_AGENTE",
  "rationale": "Sua justificativa para a escolha do agente."
}}

**Exemplos:**
- Pergunta: "Qual a correlação entre as colunas X e Y?" -> agent_to_call: "BOTH"
- Pergunta: "Existem outliers nos dados?" -> agent_to_call: "BOTH"
- Pergunta: "Faça uma análise descritiva completa" -> agent_to_call: "BOTH"
- Pergunta: "Mostre a distribuição da idade" -> agent_to_call: "BOTH"
- Pergunta: "O que esses dados significam para o meu negócio?" -> agent_to_call: "ConsultantAgent"
- Pergunta: "Me dê o código para gerar esse gráfico de barras" -> agent_to_call: "CodeGeneratorAgent"

**IMPORTANTE: Sua saída DEVE ser APENAS o objeto JSON, sem nenhum texto adicional ou formatação markdown.**
Minimize o tamanho: responda com o menor JSON válido possível (sem espaços extras).
"""

def _clean_json_output(raw_output: str) -> str:
    """
    Limpa a saída do LLM para extrair apenas o JSON, removendo o wrapper de markdown.
    """
    # Verifica se a saída contém o wrapper de código JSON
    if "```json" in raw_output:
        # Extrai o conteúdo entre ```json e ```
        clean_output = raw_output.split("```json")[1].split("```")[0].strip()
        return clean_output
    
    # Se não tiver o wrapper, mas tiver os ```, remove-os também
    if "```" in raw_output:
        clean_output = raw_output.replace("```", "").strip()
        return clean_output

    return raw_output.strip()


def get_coordinator_agent(api_key: str):
    llm = get_llm(api_key)
    prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    # Alteração: Agora usamos StrOutputParser para obter a string bruta do LLM
    chain = prompt | llm | StrOutputParser()
    return chain

def run_coordinator(api_key: str, df: pd.DataFrame, conversation_history: str, user_question: str) -> dict:
    """
    Executa o agente coordenador e garante que a saída seja um JSON válido.
    """
    agent = get_coordinator_agent(api_key)
    dataset_preview = get_dataset_preview(df)
    
    # 1. Invoca o agente para obter a resposta como string
    raw_response = agent.invoke({
        "dataset_preview": dataset_preview,
        "conversation_history": conversation_history,
        "user_question": user_question
    })
    
    # 2. Limpa a string de resposta para remover o markdown
    cleaned_response = _clean_json_output(raw_response)
    
    # 3. Tenta carregar a string limpa como um objeto JSON
    try:
        json_response = json.loads(cleaned_response)
        return json_response
    except json.JSONDecodeError as e:
        # Se falhar, isso indica um problema mais sério com a saída do LLM
        print(f"Erro ao decodificar JSON do Coordenador: {e}")
        print(f"Resposta bruta recebida: {raw_response}")
        # Retorna um dicionário de erro para evitar que a aplicação quebre
        return {
            "agent_to_call": "ErrorAgent",
            "question_for_agent": "A resposta do coordenador não foi um JSON válido.",
            "rationale": f"Erro de parsing. Resposta recebida:\n{raw_response}"
        }