# Arquivo: agents/visualization.py

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from agents.agent_setup import get_llm, get_dataset_preview
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

PROMPT_TEMPLATE = """
Você é o "VisualizationAgent", um especialista em visualização de dados. Sua tarefa é gerar o código Python para criar um gráfico interativo usando a biblioteca Plotly.

**Contexto da Análise:**
{dataset_preview}

**Análise de Dados Recebida (se houver):**
{analysis_results}

**Pedido do Usuário:**
"{user_request}"

**Sua Tarefa:**
Gere um script Python que cria a visualização solicitada.
O seu código deve assumir que um DataFrame do pandas já existe e está disponível na variável `df`.

**REGRAS IMPORTANTES:**
1.  **NÃO inclua** a linha `df = pd.read_csv(...)` no seu código. O DataFrame `df` já está carregado na memória.
2.  O código deve incluir os imports necessários, como `import plotly.express as px`.
3.  O código do gráfico deve ser claro, com títulos e labels apropriados.
4.  O código deve criar uma figura e atribuí-la a uma variável chamada `fig`. Ex: `fig = px.histogram(...)`.
5.  **NÃO inclua** a linha `fig.show()`. A aplicação se encarregará de exibir o gráfico.

**IMPORTANTE:** Retorne APENAS o bloco de código Python. Não inclua nenhuma explicação ou texto adicional.

**Exemplo de Pedido:** "Crie um histograma da coluna 'idade'."
**Exemplo de Saída Esperada:**
```python
import plotly.express as px

# O DataFrame 'df' já existe.
# A coluna 'idade' foi identificada como numérica.

fig = px.histogram(df, x='idade', title='Distribuição da Idade', nbins=20)
fig.update_layout(bargap=0.1)
"""

def generate_statistical_visualization(df: pd.DataFrame, question: str):
    """
    Gera visualizações automáticas para análises estatísticas comuns.
    Retorna código Python executável para gráficos Plotly.
    """
    question_lower = question.lower()
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    
    # 1. CORRELAÇÃO - Heatmap
    if any(word in question_lower for word in ['correlação', 'correlacao', 'relaciona', 'influência', 'influencia']):
        if len(numeric_cols) > 1:
            code = f"""
import plotly.express as px
import pandas as pd

# Calcular matriz de correlação
numeric_cols = {numeric_cols}
corr_matrix = df[numeric_cols].corr()

# Criar heatmap de correlação
fig = px.imshow(corr_matrix, 
                text_auto='.2f',
                aspect='auto',
                color_continuous_scale='RdBu_r',
                title='Matriz de Correlação entre Variáveis',
                labels=dict(color="Correlação"))
fig.update_layout(width=800, height=600)
"""
            return code
    
    # 2. OUTLIERS - Box Plot
    if any(word in question_lower for word in ['outlier', 'atípico', 'atipico', 'anomalia', 'anômalo']):
        if len(numeric_cols) > 0:
            # Limitar a 6 colunas para não sobrecarregar
            cols_to_plot = numeric_cols[:6]
            code = f"""
import plotly.express as px
import pandas as pd

# Selecionar colunas numéricas para box plot
numeric_cols = {cols_to_plot}
df_melted = df[numeric_cols].melt(var_name='Variável', value_name='Valor')

# Criar box plot para detectar outliers
fig = px.box(df_melted, 
             x='Variável', 
             y='Valor',
             title='Detecção de Outliers por Variável (Box Plot)',
             color='Variável')
fig.update_layout(showlegend=False, height=500)
"""
            return code
    
    # 3. DISTRIBUIÇÃO - Histogramas múltiplos
    if any(word in question_lower for word in ['distribuição', 'distribuicao', 'histograma', 'densidade']):
        if len(numeric_cols) > 0:
            # Pegar primeira coluna numérica ou a mais relevante
            col = numeric_cols[0]
            code = f"""
import plotly.express as px

# Criar histograma da distribuição
fig = px.histogram(df, 
                   x='{col}',
                   marginal='box',
                   title=f'Distribuição de {col}',
                   labels={{'{col}': '{col}'}},
                   nbins=50)
fig.update_layout(bargap=0.1, height=500)
"""
            return code
    
    # 4. ESTATÍSTICAS DESCRITIVAS - Box plots de todas variáveis
    if any(word in question_lower for word in ['descri', 'estatística', 'resumo', 'geral']):
        if len(numeric_cols) > 0:
            cols_to_plot = numeric_cols[:8]
            code = f"""
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Criar subplots para múltiplas variáveis
numeric_cols = {cols_to_plot}
n_cols = len(numeric_cols)
n_rows = (n_cols + 2) // 3  # 3 colunas por linha

fig = make_subplots(rows=n_rows, cols=3,
                    subplot_titles=[f'Dist. {{col}}' for col in numeric_cols])

for idx, col in enumerate(numeric_cols):
    row = idx // 3 + 1
    col_pos = idx % 3 + 1
    
    fig.add_trace(
        go.Histogram(x=df[col], name=col, showlegend=False),
        row=row, col=col_pos
    )

fig.update_layout(height=300*n_rows, 
                  title_text='Distribuições das Variáveis Numéricas',
                  showlegend=False)
"""
            return code
    
    # 5. VALORES FALTANTES - Gráfico de barras
    if any(word in question_lower for word in ['faltante', 'missing', 'nulo', 'nan', 'vazio']):
        code = """
import plotly.express as px
import pandas as pd

# Calcular valores faltantes
missing_data = pd.DataFrame({
    'Coluna': df.columns,
    'Missing': df.isnull().sum(),
    'Porcentagem': (df.isnull().sum() / len(df) * 100).round(2)
})
missing_data = missing_data[missing_data['Missing'] > 0].sort_values('Missing', ascending=False)

if not missing_data.empty:
    fig = px.bar(missing_data, 
                 x='Coluna', 
                 y='Porcentagem',
                 title='Porcentagem de Valores Faltantes por Coluna',
                 text='Porcentagem',
                 color='Porcentagem',
                 color_continuous_scale='Reds')
    fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
    fig.update_layout(height=500)
else:
    # Caso não haja missing values
    import plotly.graph_objects as go
    fig = go.Figure()
    fig.add_annotation(text="Nenhum valor faltante detectado no dataset",
                      xref="paper", yref="paper",
                      x=0.5, y=0.5, showarrow=False,
                      font=dict(size=20))
"""
        return code
    
    return None  # Nenhuma visualização automática detectada

def get_visualization_agent(api_key: str):
    llm = get_llm(api_key)
    prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    chain = prompt | llm | StrOutputParser()
    return chain

def run_visualization(api_key: str, df: pd.DataFrame, analysis_results: str, user_request: str):
    # TENTAR GERAR VISUALIZAÇÃO AUTOMÁTICA PRIMEIRO
    auto_viz_code = generate_statistical_visualization(df, user_request)
    
    if auto_viz_code:
        # Se detectou análise estatística, retornar código automático
        return auto_viz_code
    
    # Caso contrário, usar o agente LLM para gerar código customizado
    agent = get_visualization_agent(api_key)
    dataset_preview = get_dataset_preview(df)
    raw_code = agent.invoke({
        "dataset_preview": dataset_preview,
        "analysis_results": analysis_results,
        "user_request": user_request
    })

    if "```python" in raw_code:
        clean_code = raw_code.split("```python")[1].split("```")[0].strip()
    else:
        clean_code = raw_code.strip()
        
    return clean_code