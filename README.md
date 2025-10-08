# Sistema de Análise Exploratória de Dados (EDA) com Inteligência Artificial# InsightAgent EDA - Seu Assistente de Análise de Dados com IA 🤖📊



Sistema inteligente para análise exploratória de dados que utiliza agentes de IA para responder perguntas sobre arquivos CSV em linguagem natural, gerando análises estatísticas, visualizações gráficas e insights acionáveis.Uma aplicação inteligente que permite fazer perguntas sobre seus dados em linguagem natural e receber análises completas, gráficos interativos e insights acionáveis.



## 📋 Sobre o Projeto## 🎯 O que é esta aplicação?



Este projeto foi desenvolvido como parte da atividade avaliativa do curso de **Agentes Autônomos** da **I2A2 Academy** (Institut d'Intelligence Artificielle Appliquée).O **InsightAgent EDA** é uma ferramenta de análise exploratória de dados que utiliza inteligência artificial para:



**Objetivo:** Criar uma ferramenta genérica de EDA capaz de analisar qualquer arquivo CSV, responder perguntas complexas sobre os dados e fornecer conclusões inteligentes baseadas em memória contextual.- ✅ **Analisar dados automaticamente** - Faça upload de um arquivo CSV e faça perguntas em português

- ✅ **Gerar gráficos interativos** - Cria visualizações usando Plotly

## ✨ Funcionalidades Principais- ✅ **Fornecer insights de negócio** - Interpreta os dados e dá recomendações práticas

- ✅ **Gerar código Python** - Exporta análises para reutilizar em seus projetos

- **Análise Automática de Dados:** Carregue um arquivo CSV e faça perguntas em português- ✅ **Preservar histórico** - Mantém suas conversas e análises salvas na nuvem

- **Geração de Gráficos Interativos:** Visualizações criadas automaticamente com Plotly

- **Insights de Negócio:** Interpretação inteligente dos dados com recomendações práticas## 🏗️ Como Funciona?

- **Geração de Código Python:** Exportação de análises para reutilização

- **Memória de Contexto:** O sistema lembra conversas anteriores para análises mais profundasA aplicação utiliza **5 agentes especializados** que trabalham em conjunto:

- **Interface Simples e Profissional:** Design limpo sem distrações

### 1. **CoordinatorAgent** 🎯

## 🏗️ Arquitetura do Sistema- **O que faz:** Analisa sua pergunta e decide qual agente é mais adequado

- **Quando usar:** Sempre - é o agente que organiza todo o sistema

O sistema utiliza **5 agentes especializados** baseados no framework LangChain e Google Gemini 1.5 Flash:

### 2. **DataAnalystAgent** 📈

### 1. CoordinatorAgent 🎯- **O que faz:** Realiza análises estatísticas detalhadas

- **Função:** Roteia as perguntas do usuário para o agente mais adequado- **Quando usar:** Para perguntas como:

- **Tecnologia:** Google Gemini 1.5 Flash  - "Qual a média da coluna X?"

- **Decisão:** Analisa a pergunta e escolhe qual agente deve responder  - "Quantos registros temos?"

  - "Existe correlação entre as colunas A e B?"

### 2. DataAnalystAgent 📊  - "Quais são os valores únicos?"

- **Função:** Realiza análises estatísticas detalhadas

- **Capacidades:**### 3. **VisualizationAgent** 📊

  - Estatísticas descritivas (média, mediana, desvio padrão, variância)- **O que faz:** Gera código para criar gráficos interativos

  - Identificação de valores únicos e valores nulos- **Quando usar:** Para pedidos como:

  - Análise de correlação entre variáveis  - "Mostre um gráfico de barras da coluna X"

  - Detecção de outliers e anomalias  - "Crie um histograma da idade"

  - Medidas de tendência central e dispersão  - "Faça um scatter plot entre preço e tamanho"

  - "Gere um heatmap de correlação"

### 3. VisualizationAgent 📈

- **Função:** Gera código Python para criar gráficos interativos### 4. **ConsultantAgent** 💡

- **Tipos de gráficos:**- **O que faz:** Interpreta os dados e fornece insights de negócio

  - Histogramas e distribuições- **Quando usar:** Para perguntas como:

  - Gráficos de barras e colunas  - "O que esses dados significam para meu negócio?"

  - Scatter plots (dispersão)  - "Quais são as principais descobertas?"

  - Heatmaps de correlação  - "Que decisões devo tomar baseado nestes dados?"

  - Box plots e violin plots  - "Quais são os riscos e oportunidades?"

  - Gráficos de linha temporal

### 5. **CodeGeneratorAgent** ⚙️

### 4. ConsultantAgent 💡- **O que faz:** Gera código Python completo para suas análises

- **Função:** Fornece insights de negócio e recomendações estratégicas- **Quando usar:** Para pedidos como:

- **Capacidades:**  - "Me dê o código para esta análise"

  - Interpretação de tendências nos dados  - "Gere um notebook Jupyter"

  - Identificação de padrões e agrupamentos  - "Crie um script Python para automatizar isso"

  - Recomendações acionáveis

  - Análise de impacto de negócio## 🚀 Como Usar

  - Conclusões baseadas em análises anteriores

### 1. **Instalação**

### 5. CodeGeneratorAgent ⚙️

- **Função:** Gera código Python completo para automatização```bash

- **Saída:** Scripts reutilizáveis e notebooks Jupyter exportáveis# 1. Clone o repositório

cd rhein-ai-agent-challenge

## 🛠️ Tecnologias Utilizadas

# 2. Crie um ambiente virtual

| Tecnologia | Versão | Propósito |python -m venv .venv

|-----------|--------|-----------|

| **Python** | 3.8+ | Linguagem principal |# 3. Ative o ambiente

| **Streamlit** | 1.30.0+ | Interface web |# Windows:

| **LangChain** | 0.1.0+ | Framework de agentes |.venv\Scripts\activate

| **Google Gemini** | 1.5 Flash | Modelo de IA |# Linux/Mac:

| **Pandas** | 2.0.0+ | Manipulação de dados |# 4. Instale as dependências

| **Plotly** | 5.18.0+ | Visualizações interativas |pip install -r requirements.txt

| **NumPy** | 1.24.0+ | Computação numérica |```toml

| **Scikit-learn** | 1.3.0+ | Análises estatísticas |[custom]

| **Supabase** | 2.0.0+ | Banco de dados (opcional) |google_api_key = "sua_chave_aqui"

supabase_url = "https://seu-projeto.supabase.co"

## 🚀 Instalação e Configuraçãosupabase_key = "sua_chave_supabase_aqui"

```

### Pré-requisitos

#### **Método 2: Variáveis de Ambiente**

- Python 3.8 ou superior instalado

- Chave da API do Google Gemini ([obter gratuitamente aqui](https://makersuite.google.com/app/apikey))Crie um arquivo `.env` baseado no `.env.example`:

- Git (opcional, para clonar o repositório)

- Editor de texto (VS Code, Notepad++, etc.)```bash

cp .env.example .env

### Passo 1: Obter os Arquivos```



**Opção A - Clonar com Git:**Edite o `.env` com suas chaves:

```bash- **GOOGLE_API_KEY**: Obtenha em [Google AI Studio](https://makersuite.google.com/app/apikey)

git clone https://github.com/SEU_USUARIO/ai-agent-challenge.git- **SUPABASE_URL** e **SUPABASE_KEY**: Obtenha em [Supabase Dashboard](https://supabase.com/dashboard)

cd ai-agent-challenge

```### 3. **Executar a Aplicação**



**Opção B - Download Manual:**```bash

1. Baixe o arquivo ZIP do GitHubstreamlit run app.py

2. Extraia para uma pasta de sua escolha```

3. Abra o terminal/prompt nessa pasta

Acesse a aplicação no navegador em `http://localhost:8501`

### Passo 2: Criar Ambiente Virtual (Recomendado)

### 4. **Usando a Aplicação**

```bash

# Windows (PowerShell ou CMD)1. **Upload do CSV**: Arraste seu arquivo CSV para a área lateral

python -m venv .venv2. **Faça perguntas**: Digite suas perguntas em português na caixa de chat

.venv\Scripts\activate3. **Explore sugestões**: Clique nas sugestões de perguntas que aparecem

## 💡 Exemplos Práticos

# Linux/Mac

python3 -m venv .venv### **Exemplo 1: Análise de Vendas**

source .venv/bin/activate```

```Dataset: vendas.csv (colunas: produto, categoria, valor, data, região)



**Por que usar ambiente virtual?**Perguntas que você pode fazer:

- Isola as dependências do projeto- "Qual foi o produto mais vendido no último trimestre?"

- Evita conflitos com outros projetos Python- "Mostre um gráfico de barras das vendas por categoria"

- Facilita a reprodução do ambiente- "Qual é a correlação entre valor e região?"

- "O que esses dados indicam sobre o desempenho regional?"

### Passo 3: Instalar Dependências- "Gere o código para analisar a sazonalidade das vendas"

```

```bash

pip install -r requirements.txt### **Exemplo 2: Análise de Recursos Humanos**

``````

Dataset: funcionarios.csv (colunas: nome, idade, salario, departamento, tempo_casa)

**Nota:** A instalação pode demorar alguns minutos na primeira vez.

Perguntas que você pode fazer:

### Passo 4: Configurar Chaves da API- "Qual é a distribuição salarial por departamento?"

- "Crie um histograma da idade dos funcionários"

**PASSO IMPORTANTE - NÃO PULE!**- "Quantos funcionários temos em cada departamento?"

- "Existe correlação entre tempo de casa e salário?"

1. Crie a pasta `.streamlit` na raiz do projeto:- "Quais insights podemos tirar sobre retenção de talentos?"

```bash```

# Windows

mkdir .streamlit### **Exemplo 3: Análise de Marketing**

```

# Linux/MacDataset: campanhas.csv (colunas: campanha, canal, investimento, conversoes, receita)

mkdir .streamlit

```Perguntas que você pode fazer:

- "Qual canal de marketing tem o melhor ROI?"

2. Crie o arquivo `.streamlit/secrets.toml` com o seguinte conteúdo:- "Mostre um scatter plot entre investimento e receita"

- "O que os dados dizem sobre a efetividade das campanhas?"

```toml- "Gere código para calcular métricas de performance"

[custom]- "Quais campanhas devemos investir mais?"

google_api_key = "COLE_SUA_CHAVE_AQUI"```

supabase_url = ""

supabase_key = ""### **Datasets de Exemplo para Testar**

```

Se você não tem dados próprios, pode usar estes datasets públicos:

3. **Substitua** `COLE_SUA_CHAVE_AQUI` pela sua chave real do Google

1. **Titanic Dataset** (sobreviventes do Titanic)

**Onde obter a chave da API:**   - [Baixar CSV](https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv)

1. Acesse: https://makersuite.google.com/app/apikey

2. Faça login com sua conta Google2. **Iris Dataset** (flores - dados científicos)

3. Clique em "Create API key"   - [Baixar CSV](https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv)

4. Copie a chave gerada (começa com `AIza...`)

5. Cole no arquivo `secrets.toml`3. **Wine Quality** (avaliação de vinhos)

   - [Baixar CSV](https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv)

**Sobre o Supabase:**

- **É OPCIONAL** - deixe os campos vazios se não quiser usar4. **House Prices** (preços de imóveis)

- Serve apenas para salvar histórico de conversas   - [Baixar CSV](https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv)

- O sistema funciona 100% sem ele

### **Obrigatórios**

### Passo 5: Executar a Aplicação- ✅ Python 3.8 ou superior

- ✅ Chave da API do Google Gemini

```bash

python -m streamlit run app.py### **Opcionais (mas recomendados)**

```- ✅ Conta no Supabase (para salvar histórico)

- ✅ Git (para controle de versão)

**OU (se o comando acima não funcionar):**

## 🔧 Dependências Principais

```bash

streamlit run app.py| Biblioteca | Propósito |

```|------------|-----------|

| `streamlit` | Interface web da aplicação |

A aplicação abrirá automaticamente no navegador em: `http://localhost:8501`| `langchain` | Framework para agentes de IA |

| `google-generativeai` | Modelo de IA (Gemini) |

**Se não abrir automaticamente:**| `pandas` | Manipulação de dados |

1. Abra seu navegador| `plotly` | Criação de gráficos interativos |

2. Digite na barra de endereços: `http://localhost:8501`| `supabase` | Banco de dados para histórico |



## 📖 Como Usar## 🎨 Funcionalidades Avançadas



### Uso Básico### **Cache Inteligente**

- Os gráficos são armazenados em cache para evitar recriação desnecessária

1. **Acesse a aplicação** no navegador (`http://localhost:8501`)- Melhora a performance e reduz custos com API

2. **Faça upload de um arquivo CSV:**

   - Clique em "Browse files" na barra lateral### **Histórico Persistente**

   - Selecione seu arquivo CSV- Suas conversas e análises são salvas automaticamente

   - Aguarde o carregamento (alguns segundos)- Recupere sessões anteriores a qualquer momento

3. **Visualize os dados:**

   - Preview dos dados será exibido automaticamente### **Sugestões Dinâmicas**

   - Estatísticas básicas aparecem abaixo- A IA sugere perguntas relevantes baseadas no contexto

4. **Faça perguntas:**- Melhora a experiência de exploração dos dados

   - Use a caixa de chat na parte inferior

   - Digite sua pergunta em português### **Execução Segura de Código**

   - Pressione Enter ou clique no botão- O código Python gerado é executado em ambiente isolado

5. **Explore sugestões:**- Previne execução de código malicioso

   - Botões com sugestões aparecem acima do chat

   - Clique em qualquer sugestão para usar## 🛠️ Estrutura do Projeto

6. **Visualize resultados:**

   - Análises aparecem como texto```

   - Gráficos são renderizados automaticamenterhein-ai-agent-challenge/

   - Código Python pode ser gerado e exportado├── agents/              # Agentes especializados de IA

│   ├── coordinator.py   # Decide qual agente usar

### Exemplos de Perguntas│   ├── data_analyst.py  # Análises estatísticas

│   ├── visualization.py # Geração de gráficos

#### 📊 Descrição dos Dados│   ├── consultant.py    # Insights de negócio

- "Quais são os tipos de dados de cada coluna?"│   └── code_generator.py # Geração de código

- "Mostre as estatísticas descritivas completas"├── components/          # Componentes da interface

- "Qual é o intervalo de valores da coluna Amount?"│   ├── ui_components.py # Elementos visuais

- "Quantos valores nulos existem em cada coluna?"│   └── suggestion_generator.py # Sugestões inteligentes

- "Qual é a média e mediana da coluna Time?"├── utils/              # Utilitários e helpers

│   ├── config.py       # Configurações da app

#### 📈 Identificação de Padrões│   ├── data_loader.py  # Carregamento de CSVs

- "Existem padrões temporais nos dados?"│   ├── memory.py       # Integração com banco

- "Quais são os valores mais frequentes na coluna Class?"│   └── chart_cache.py  # Cache de gráficos

- "Identifique agrupamentos nos dados"├── app.py              # Arquivo principal

- "Há alguma tendência nos dados de V1 a V28?"├── requirements.txt    # Dependências Python

└── README.md          # Este arquivo

#### 🔍 Detecção de Anomalias```

- "Existem outliers na coluna Amount?"

- "Identifique valores atípicos em todas as colunas"## 📊 Tipos de Análise Suportados

- "Como os outliers afetam a análise?"

- "Quais transações podem ser consideradas anômalas?"### **Análises Estatísticas**

- Estatísticas descritivas (média, mediana, desvio padrão)

#### 🔗 Relações entre Variáveis- Contagem de valores únicos e nulos

- "Mostre um gráfico de correlação entre todas as variáveis"- Identificação de outliers

- "Qual é a correlação entre V1 e Amount?"- Análise de correlação

- "Crie um scatter plot entre Time e Amount"- Testes de hipóteses

- "Existe relação entre as colunas V1 a V10?"

- "Quais variáveis têm maior correlação com Class?"### **Visualizações Disponíveis**

- Histogramas e distribuições

#### 💡 Conclusões e Insights- Gráficos de barras e colunas

- "Quais são as principais conclusões desta análise?"- Scatter plots e dispersão

- "O que os dados indicam sobre fraudes?"- Box plots e violin plots

- "Resuma os insights mais importantes"- Heatmaps de correlação

- "Que recomendações você pode fazer?"- Gráficos de linha e área



#### 📊 Visualizações Específicas### **Insights de Negócio**

- "Crie um histograma da coluna Amount"- Interpretação de tendências

- "Mostre um box plot das variáveis V1 a V5"- Identificação de padrões

- "Gere um heatmap de correlação"- Recomendações estratégicas

- "Faça um gráfico de barras para Class"- Análise de oportunidades

- Detecção de anomalias

## 🌐 Deploy no Streamlit Cloud

## 🔒 Segurança e Privacidade

### ❓ PERGUNTA IMPORTANTE: Preciso do Supabase?

- ✅ **Dados locais**: Seus arquivos CSV ficam apenas no seu computador

**RESPOSTA: NÃO! Você NÃO precisa do Supabase!**- ✅ **Código isolado**: Análises são executadas em ambiente seguro

- ✅ **API keys protegidas**: Configurações sensíveis são criptografadas

**O Supabase é 100% OPCIONAL.**- ✅ **Histórico opcional**: Use Supabase apenas se quiser salvar conversas



O sistema funciona perfeitamente sem ele. O Supabase é usado APENAS para:## 🆘 Suporte e Troubleshooting

- ✅ Salvar histórico de conversas entre sessões

- ✅ Recuperar análises antigas### **Problemas Comuns**



**Se você NÃO configurar o Supabase:****1. "Chave da API não configurada"**

- ✅ Todas as análises funcionam normalmente```bash

- ✅ Gráficos são gerados corretamente# Verifique se a chave está no arquivo .streamlit/secrets.toml

- ✅ Perguntas são respondidas com precisão# ou nas variáveis de ambiente

- ✅ Memória funciona durante a sessão ativa```

- ❌ Histórico não fica salvo após fechar o navegador

**2. "Erro ao carregar CSV"**

### Como fazer Deploy no Streamlit Cloud (GRÁTIS)- Verifique se o arquivo é um CSV válido

- Certifique-se de que tem pelo menos uma linha de dados

#### Passo 1: Preparar o Repositório GitHub- Arquivos muito grandes podem precisar de mais memória



1. **Crie uma conta no GitHub** (se ainda não tiver):**3. "Gráfico não aparece"**

   - Acesse: https://github.com- Aguarde alguns segundos após fazer a pergunta

   - Clique em "Sign up"- Verifique se há dados suficientes para o tipo de gráfico

- Tente reformular a pergunta

2. **Crie um novo repositório:**

   - Clique no "+" no canto superior direito### **Logs e Debug**

   - Selecione "New repository"

   - Nome: `ai-agent-challenge` (ou outro nome)Para ver logs detalhados:

   - Marque como "Public"```python

   - Clique em "Create repository"# Execute com debug habilitado

DEBUG_MODE = True  # No arquivo app.py, linha 31

3. **Faça upload dos arquivos:**```

   - Opção A - Pela interface web do GitHub (arraste e solte)

   - Opção B - Via Git (se souber usar)## ❓ FAQ - Perguntas Frequentes



#### Passo 2: Deploy no Streamlit Cloud### **🔑 Configuração e API**



1. **Crie uma conta no Streamlit Cloud:****P: Como obter a chave da API do Google Gemini?**

   - Acesse: https://streamlit.io/cloud```

   - Clique em "Sign up"R: Acesse https://makersuite.google.com/app/apikey

   - Faça login com sua conta GitHub   Clique em "Create API key"

   Copie a chave gerada e configure no .streamlit/secrets.toml

2. **Conecte seu repositório:**```

   - Clique em "New app"

   - Selecione seu repositório do GitHub**P: A aplicação funciona sem o Supabase?**

   - Escolha a branch: `main` (ou `master`)```

   - Defina o arquivo principal: `app.py`R: Sim! O Supabase é opcional e serve apenas para salvar o histórico.

   Você pode usar a aplicação normalmente sem ele.

3. **Configure os Secrets (IMPORTANTE):**```

   - Clique em "Advanced settings"

   - Na seção "Secrets", cole:**P: Quais são os custos da API do Google?**

   ```

   ```tomlR: O Google Gemini tem uma cota gratuita generosa.

   [custom]   Para uso básico, dificilmente você gastará algo.

   google_api_key = "SUA_CHAVE_AQUI"   Consulte: https://ai.google.dev/pricing

   supabase_url = ""```

   supabase_key = ""

   ```### **📊 Dados e Análises**

   

   - **Substitua** `SUA_CHAVE_AQUI` pela sua chave real**P: Quais formatos de arquivo são suportados?**

   - **Deixe Supabase vazio** (a menos que queira usar)```

R: Atualmente apenas arquivos CSV.

4. **Deploy:**   Certifique-se de que o arquivo tem extensão .csv

   - Clique em "Deploy!"   e está separado por vírgulas.

   - Aguarde 3-5 minutos (primeira vez demora mais)```

   - Sua aplicação estará disponível em: `https://SEU-APP.streamlit.app`

**P: Há limite de tamanho para os arquivos?**

5. **Compartilhe o link:**```

   - Copie o link geradoR: Não há limite técnico, mas arquivos muito grandes (>100MB)

   - Compartilhe com quem quiser   podem causar lentidão. Recomendamos começar com datasets menores.

   - Qualquer pessoa pode acessar!```



## 📁 Estrutura do Projeto**P: Posso fazer perguntas em português?**

```

```R: Sim! A aplicação está configurada para funcionar em português.

ai-agent-challenge/   Você pode fazer perguntas naturalmente em português brasileiro.

├── app.py                      # Aplicação principal Streamlit```

├── requirements.txt            # Lista de dependências Python

├── README.md                   # Este arquivo (documentação)### **🔧 Problemas Técnicos**

├── LICENSE                     # Licença MIT

│**P: A aplicação não inicia. O que fazer?**

├── .streamlit/                 # Configurações (NÃO COMMITAR)```

│   └── secrets.toml           # Chaves da API (manter privado!)R: 1. Verifique se todas as dependências estão instaladas

│   2. Confirme se a chave da API está configurada

├── agents/                     # Módulos dos agentes de IA   3. Tente: pip install -r requirements.txt

│   ├── __init__.py               4. Reinicie o ambiente virtual

│   ├── agent_setup.py          # Configuração base dos agentes```

│   ├── coordinator.py          # Agente coordenador (roteamento)

│   ├── data_analyst.py         # Agente analista de dados**P: Os gráficos não aparecem. Como resolver?**

│   ├── visualization.py        # Agente de visualização```

│   ├── consultant.py           # Agente consultor (insights)R: 1. Aguarde alguns segundos após fazer a pergunta

│   └── code_generator.py       # Agente gerador de código   2. Verifique se há dados suficientes para o gráfico

│   3. Tente reformular a pergunta

├── components/                 # Componentes da interface   4. Verifique o console por erros

│   ├── __init__.py```

│   ├── ui_components.py        # Elementos visuais (sidebar, chat)

│   ├── notebook_generator.py   # Exportação de notebooks Jupyter**P: As sugestões de perguntas não aparecem**

│   └── suggestion_generator.py # Geração de sugestões inteligentes```

│R: 1. Certifique-se de que há histórico de conversa

└── utils/                      # Utilitários auxiliares   2. Verifique se a chave da API está funcionando

    ├── __init__.py   3. Tente recarregar a página

    ├── config.py               # Carregamento de configurações```

    ├── data_loader.py          # Carregamento e validação de CSV

    ├── memory.py               # Integração com Supabase (opcional)### **🚀 Uso Avançado**

    └── chart_cache.py          # Cache de gráficos (performance)

```**P: Como exportar o código gerado?**

```

## ❓ Perguntas Frequentes (FAQ)R: O código aparece automaticamente na conversa.

   Você pode copiá-lo e colar em seu editor de código.

### Configuração```



**P: Preciso do Supabase para usar o sistema?****P: Posso usar meus próprios modelos de IA?**

```

R: **NÃO!** O Supabase é completamente opcional. O sistema funciona 100% sem ele. É usado apenas para salvar histórico de conversas entre sessões.R: Atualmente a aplicação usa Google Gemini.

   Para outros modelos, seria necessário modificar o código.

**P: Como obter a chave da API do Google Gemini?**```



R: **P: Como contribuir com o projeto?**

1. Acesse: https://makersuite.google.com/app/apikey```

2. Faça login com sua conta GoogleR: 1. Faça um fork no GitHub

3. Clique em "Create API key"   2. Crie uma branch para sua feature

4. Copie a chave gerada (começa com `AIza...`)   3. Teste suas mudanças

5. Cole no arquivo `.streamlit/secrets.toml`   4. Abra um Pull Request

```

**P: A chave da API é gratuita?**

### **📈 Performance**

R: Sim! O Google Gemini oferece uma cota gratuita generosa de 60 requisições por minuto.

**P: Por que a aplicação está lenta?**

### Uso```

R: 1. Datasets muito grandes podem causar lentidão

**P: A aplicação funciona com qualquer arquivo CSV?**   2. Muitas perguntas simultâneas

   3. Limitações da API gratuita

R: Sim! O sistema foi projetado para ser genérico e trabalhar com qualquer CSV válido, independente das colunas.   4. Hardware insuficiente

```

**P: Posso fazer perguntas em inglês?**

**P: Como melhorar a performance?**

R: Sim, mas o sistema foi otimizado para português. Respostas em português são mais precisas.```

R: 1. Use datasets menores para começar

**P: Quantas linhas o CSV pode ter?**   2. Faça perguntas mais específicas

   3. Aguarde entre perguntas

R: Tecnicamente ilimitado, mas recomendamos:   4. Considere usar cache local

- **Ótimo:** até 10.000 linhas```

- **Bom:** 10.000 - 100.000 linhas

- **Lento:** acima de 100.000 linhas## 🔒 Limitações Conhecidas



### CustosEste é um projeto de aprendizado e exploração. Sugestões são bem-vindas!



**P: Quanto custa usar o sistema?**1. Faça um fork do projeto

2. Crie uma branch para sua feature

R: **TOTALMENTE GRATUITO!**3. Commit suas mudanças

- Google Gemini: Cota gratuita (60 req/min)4. Push para a branch

- Streamlit Cloud: Gratuito para projetos públicos5. Abra um Pull Request

- Supabase: Gratuito até 500MB (opcional)

## 📄 Licença

**P: Há limite de uso?**

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para detalhes.

R: Sim, os limites da cota gratuita do Google:

- 60 requisições por minuto## 🙏 Agradecimentos

- 1.500 requisições por dia

- Suficiente para uso normal- **Google Gemini** pela inteligência artificial

- **Streamlit** pela incrível framework web

### Problemas Técnicos- **LangChain** pela abstração de agentes

- **Plotly** pelas visualizações interativas

**P: Erro "Chave da API não configurada"**- **Supabase** pelo banco de dados em tempo real



R: Verifique se:---

1. O arquivo `.streamlit/secrets.toml` existe

2. A chave está no formato correto**Desenvolvido com ❤️ para democratizar a análise de dados**

3. Você colocou a chave REAL (não o texto de exemplo)

**P: CSV não carrega**

R: Verifique se:
1. O arquivo é realmente um CSV (não Excel)
2. Está separado por vírgulas
3. Tem cabeçalhos na primeira linha
4. Não está corrompido

**P: Gráficos não aparecem**

R:
1. Aguarde alguns segundos (análise demora)
2. Recarregue a página (F5)
3. Verifique se há dados suficientes
4. Tente reformular a pergunta

**P: Aplicação está lenta**

R: Possíveis soluções:
1. Use um CSV menor para testes
2. Faça perguntas mais específicas
3. Limpe o cache do navegador
4. Reinicie a aplicação

## 🔒 Segurança e Privacidade

### Proteção de Dados

- ✅ **Dados locais:** Seus arquivos CSV ficam no seu computador
- ✅ **Sem upload:** Dados não são enviados para servidores (exceto metadados para a API)
- ✅ **Processamento local:** Toda análise é feita na sua máquina
- ✅ **Código isolado:** Execução em ambiente seguro

### Proteção de Chaves

- ⚠️ **NUNCA** compartilhe suas chaves de API publicamente
- ⚠️ **NUNCA** faça commit do arquivo `secrets.toml` no GitHub
- ⚠️ **SEMPRE** use secrets no Streamlit Cloud
- ✅ Adicione `.streamlit/secrets.toml` ao `.gitignore`

### Dados Enviados para APIs

**O que é enviado para o Google:**
- Perguntas do usuário
- Estrutura básica dos dados (nomes de colunas, tipos)
- Estatísticas agregadas (não os dados brutos)

**O que NÃO é enviado:**
- Conteúdo completo do CSV
- Dados sensíveis linha por linha
- Informações pessoais identificáveis

## 🐛 Solução de Problemas Comuns

### Erro: ModuleNotFoundError

**Problema:** Biblioteca não instalada

**Solução:**
```bash
pip install -r requirements.txt
```

### Erro: streamlit: command not found

**Problema:** Streamlit não está no PATH

**Solução:**
```bash
python -m streamlit run app.py
```

### Erro: API key not configured

**Problema:** Chave da API não foi configurada

**Solução:**
1. Crie o arquivo `.streamlit/secrets.toml`
2. Adicione sua chave da API
3. Reinicie a aplicação

### Erro: File encoding not supported

**Problema:** CSV com encoding incorreto

**Solução:**
1. Abra o CSV no Excel/LibreOffice
2. Salve como "CSV UTF-8"
3. Tente novamente

### Aplicação não inicia

**Soluções:**
1. Verifique se Python está instalado: `python --version`
2. Ative o ambiente virtual: `.venv\Scripts\activate`
3. Reinstale dependências: `pip install -r requirements.txt`
4. Verifique se a porta 8501 não está em uso

## 📄 Licença

Este projeto está sob a licença **MIT**. Veja o arquivo `LICENSE` para detalhes.

**Resumo da licença MIT:**
- ✅ Uso comercial permitido
- ✅ Modificação permitida
- ✅ Distribuição permitida
- ✅ Uso privado permitido
- ⚠️ Sem garantia
- ⚠️ Responsabilidade do autor limitada

## 👨‍💻 Autor

Desenvolvido como projeto avaliativo para **I2A2 Academy**.

**Contato para dúvidas:** challenges@i2a2.academy

## 🙏 Agradecimentos

- **I2A2 Academy** - Institut d'Intelligence Artificielle Appliquée
- **Google** - Pelo modelo Gemini e API gratuita
- **Streamlit** - Pela incrível framework de interfaces
- **LangChain** - Pela abstração de agentes de IA
- **Plotly** - Pelas visualizações interativas
- **Comunidade Open Source** - Por todas as ferramentas utilizadas

## 📚 Referências

- [LangChain Documentation](https://python.langchain.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Google Gemini API](https://ai.google.dev/)
- [Pandas Documentation](https://pandas.pydata.org/)
- [Plotly Documentation](https://plotly.com/python/)

---

**Versão:** 2.0.0  
**Última atualização:** Outubro de 2025  
**Status:** ✅ Produção  

**Link para teste:** _(Será adicionado após deploy)_
