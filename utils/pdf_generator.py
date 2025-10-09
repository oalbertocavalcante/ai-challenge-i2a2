"""
Gerador de Relatório em PDF
Gera relatório técnico completo da análise de dados
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image, Preformatted
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from datetime import datetime
import pytz
import io
import re
import tempfile
import os

def extract_markdown_tables(text):
    """
    Extrai tabelas Markdown do texto e retorna lista de tabelas.
    Retorna: lista de tuplas (tabela_como_lista, posição_no_texto)
    """
    tables = []
    
    # Regex para detectar tabelas Markdown
    # Formato: | Col1 | Col2 |
    #          |------|------|
    #          | Val1 | Val2 |
    table_pattern = r'(\|.+\|[\r\n]+\|[-:\s|]+\|[\r\n]+(?:\|.+\|[\r\n]*)+)'
    
    matches = re.finditer(table_pattern, text, re.MULTILINE)
    
    for match in matches:
        table_text = match.group(1)
        lines = [line.strip() for line in table_text.split('\n') if line.strip()]
        
        if len(lines) < 2:  # Precisa ter pelo menos cabeçalho e separador
            continue
        
        # Processar linhas da tabela
        table_data = []
        for i, line in enumerate(lines):
            if i == 1:  # Pular linha separadora (|-----|-----|)
                continue
            
            # Extrair células (dividir por |, remover vazias)
            cells = [cell.strip() for cell in line.split('|') if cell.strip()]
            if cells:
                table_data.append(cells)
        
        if len(table_data) >= 2:  # Pelo menos cabeçalho + 1 linha de dados
            tables.append((table_data, match.start(), match.end()))
    
    return tables

def create_reportlab_table(table_data):
    """
    Converte dados de tabela em objeto Table do ReportLab com estilo.
    """
    if not table_data or len(table_data) < 1:
        return None
    
    # Criar tabela ReportLab
    t = Table(table_data, repeatRows=1)
    
    # Estilo da tabela
    style = TableStyle([
        # Cabeçalho
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2E5C8A')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('TOPPADDING', (0, 0), (-1, 0), 8),
        
        # Corpo da tabela
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
        ('TOPPADDING', (0, 1), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        
        # Bordas
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('LINEBELOW', (0, 0), (-1, 0), 1.5, colors.HexColor('#2E5C8A')),
        
        # Linhas alternadas
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F5F5F5')]),
    ])
    
    t.setStyle(style)
    return t

def create_pdf_report(messages, dataset_name, participant_name="Alberto Côrtes Cavalcante"):
    """
    Gera relatório em PDF com toda a conversa
    
    Args:
        messages: Lista de mensagens do chat
        dataset_name: Nome do dataset analisado
        participant_name: Nome do participante
    
    Returns:
        BytesIO: Buffer com o PDF gerado
    """
    buffer = io.BytesIO()
    
    # Configuração do documento
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )
    
    # Estilos
    styles = getSampleStyleSheet()
    
    # Estilo customizado para título
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=colors.HexColor('#1F4788'),
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    # Estilo para subtítulos
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#2E5C8A'),
        spaceAfter=10,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    # Estilo para texto normal
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=10,
        alignment=TA_JUSTIFY,
        spaceAfter=8
    )
    
    # Estilo para informações
    info_style = ParagraphStyle(
        'InfoStyle',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.HexColor('#555555'),
        spaceAfter=6,
        alignment=TA_LEFT
    )
    
    # Estilo para perguntas do usuário
    user_style = ParagraphStyle(
        'UserStyle',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor('#1F4788'),
        fontName='Helvetica-Bold',
        spaceAfter=6,
        leftIndent=10
    )
    
    # Estilo para respostas do assistente
    assistant_style = ParagraphStyle(
        'AssistantStyle',
        parent=styles['Normal'],
        fontSize=10,
        alignment=TA_JUSTIFY,
        spaceAfter=10,
        leftIndent=10
    )
    
    # Construir elementos do PDF
    elements = []
    
    # ===== CAPA =====
    elements.append(Spacer(1, 3*cm))
    elements.append(Paragraph("Agentes Autônomos – Relatório da Atividade Extra", title_style))
    elements.append(Spacer(1, 0.5*cm))
    elements.append(Paragraph("Análise Exploratória de Dados com Agentes de IA", subtitle_style))
    elements.append(Spacer(1, 2*cm))
    
    # Data e hora no fuso horário de São Paulo
    sao_paulo_tz = pytz.timezone('America/Sao_Paulo')
    now_sp = datetime.now(sao_paulo_tz)
    
    # Tabela de informações
    data = [
        ['Participante:', participant_name],
        ['Dataset Analisado:', dataset_name or 'N/A'],
        ['Data de Geração:', now_sp.strftime('%d/%m/%Y %H:%M:%S') + ' (Horário de São Paulo)'],
        ['Repositório GitHub:', 'https://github.com/oalbertocavalcante/ai-challenge-i2a2'],
        ['Sistema Online:', 'https://ai-challenge-i2a2.streamlit.app/'],
    ]
    
    table = Table(data, colWidths=[5*cm, 11*cm])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#E8F4F8')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ]))
    
    elements.append(table)
    elements.append(Spacer(1, 2*cm))
    
    # Rodapé da capa
    elements.append(Paragraph(
        "I2A2 Academy - Institut d'Intelligence Artificielle Appliquée",
        info_style
    ))
    elements.append(Paragraph(
        "Curso: Agentes Autônomos",
        info_style
    ))
    
    elements.append(PageBreak())
    
    # ===== 1. FRAMEWORK ESCOLHIDA =====
    elements.append(Paragraph("1. FRAMEWORK ESCOLHIDA", subtitle_style))
    elements.append(Spacer(1, 0.3*cm))
    
    framework_text = """
    <b>Framework Selecionada: LangChain + Google Gemini 1.5 Flash</b><br/><br/>
    
    A solução foi desenvolvida utilizando a framework <b>LangChain 0.3.27</b> integrada com o modelo de 
    linguagem <b>Google Gemini 1.5 Flash</b>. Esta combinação foi escolhida pelos seguintes motivos:<br/><br/>
    
    <b>• LangChain:</b> Framework Python especializada em construção de aplicações com LLMs, oferecendo 
    abstrações para chains, agents, prompts e memória contextual. Permite orquestração complexa de 
    múltiplos agentes especializados.<br/><br/>
    
    <b>• Google Gemini 1.5 Flash:</b> Modelo de IA multimodal de última geração da Google, com contexto 
    de 1 milhão de tokens, latência baixa (~2-3 segundos por resposta) e capacidade de raciocínio avançado 
    para análise de dados.<br/><br/>
    
    <b>• Streamlit 1.50.0:</b> Framework de interface web em Python para deploy rápido e interface 
    interativa com o usuário.<br/><br/>
    
    <b>Bibliotecas Complementares:</b><br/>
    • <b>Pandas 2.0+:</b> Manipulação e análise de dados<br/>
    • <b>Plotly 5.18+:</b> Visualizações interativas<br/>
    • <b>NumPy, SciPy, Scikit-learn:</b> Computação científica e estatística<br/>
    • <b>ReportLab 4.0+:</b> Geração de relatórios em PDF<br/>
    • <b>Tabulate:</b> Formatação de tabelas Markdown<br/>
    """
    
    elements.append(Paragraph(framework_text, normal_style))
    elements.append(Spacer(1, 0.5*cm))
    
    elements.append(PageBreak())
    
    # ===== 2. ESTRUTURA DA SOLUÇÃO =====
    elements.append(Paragraph("2. ESTRUTURA DA SOLUÇÃO", subtitle_style))
    elements.append(Spacer(1, 0.3*cm))
    
    structure_text = """
    <b>2.1 Arquitetura de Agentes Especializados</b><br/><br/>
    
    O sistema implementa uma arquitetura multi-agente com 5 agentes especializados coordenados 
    por um agente orquestrador:<br/><br/>
    
    <b>1. CoordinatorAgent (Orquestrador):</b><br/>
    • Analisa a intenção do usuário através de processamento de linguagem natural<br/>
    • Roteia a pergunta para o agente mais adequado<br/>
    • Implementa roteamento inteligente "BOTH" para análises estatísticas (tabela + gráfico)<br/>
    • Utiliza JSON parsing para decisões estruturadas<br/><br/>
    
    <b>2. DataAnalystAgent (Analista de Dados):</b><br/>
    • Executa análises estatísticas descritivas automaticamente<br/>
    • Gera tabelas reais usando Pandas: describe(), corr(), outliers (IQR), value_counts()<br/>
    • Converte DataFrames para formato Markdown para visualização<br/>
    • Calcula métricas: médias, medianas, desvios, correlações, p-values<br/>
    • Detecta outliers usando método IQR (Q1-1.5*IQR, Q3+1.5*IQR)<br/><br/>
    
    <b>3. VisualizationAgent (Visualização):</b><br/>
    • Gera código Python/Plotly para gráficos interativos<br/>
    • Implementa visualizações automáticas para análises estatísticas:<br/>
      - Heatmaps para correlação<br/>
      - Box plots para detecção de outliers<br/>
      - Histogramas para distribuições<br/>
      - Subplots múltiplos para análises descritivas<br/>
    • Executa código em sandbox seguro e renderiza gráficos<br/><br/>
    
    <b>4. ConsultantAgent (Consultor de Negócios):</b><br/>
    • Fornece insights e conclusões baseadas em evidências<br/>
    • Acessa memória completa de análises anteriores (all_analyses_history)<br/>
    • Gera recomendações estratégicas e acionáveis<br/>
    • Valida hipóteses com base em análises estatísticas prévias<br/><br/>
    
    <b>5. CodeGeneratorAgent (Gerador de Código):</b><br/>
    • Exporta análises como Jupyter Notebooks (.ipynb)<br/>
    • Gera código Python reproduzível e documentado<br/>
    • Inclui imports, carregamento de dados e visualizações<br/><br/>
    
    <b>2.2 Implementação de Memória Contextual</b><br/><br/>
    
    O sistema mantém dois tipos de memória na sessão:<br/>
    • <b>conversation_history:</b> Histórico completo de perguntas e respostas<br/>
    • <b>all_analyses_history:</b> Buffer com todas as análises realizadas, passado para 
    todos os agentes para contexto cumulativo<br/><br/>
    
    Esta memória permite que o ConsultantAgent gere conclusões fundamentadas em TODAS as 
    análises da sessão, não apenas a última pergunta.<br/><br/>
    
    <b>2.3 Fluxo de Execução</b><br/><br/>
    
    1. Usuário faz upload do arquivo CSV<br/>
    2. Sistema carrega dados com Pandas e armazena em st.session_state<br/>
    3. Usuário digita pergunta no chat<br/>
    4. CoordinatorAgent analisa intenção e roteia para agente(s) adequado(s)<br/>
    5. Agente(s) processa(m) pergunta com contexto de memória<br/>
    6. Sistema executa código gerado (visualizações, análises)<br/>
    7. Resposta (texto + tabelas + gráficos) é exibida ao usuário<br/>
    8. Análise é armazenada na memória para consultas futuras<br/>
    9. Usuário pode baixar conversa completa como PDF<br/>
    """
    
    elements.append(Paragraph(structure_text, normal_style))
    elements.append(Spacer(1, 0.5*cm))
    
    elements.append(PageBreak())
    
    # ===== 3. PERGUNTAS E RESPOSTAS (MÍNIMO 4, 1 COM GRÁFICO) =====
    elements.append(Paragraph("3. PERGUNTAS E RESPOSTAS DA ANÁLISE", subtitle_style))
    elements.append(Spacer(1, 0.3*cm))
    
    if not messages or len(messages) == 0:
        elements.append(Paragraph(
            "Nenhuma análise foi realizada nesta sessão.",
            normal_style
        ))
    else:
        elements.append(Paragraph(
            f"Total de interações: <b>{len(messages)}</b>",
            info_style
        ))
        elements.append(Spacer(1, 0.3*cm))
        
        # Adicionar cada mensagem
        for idx, message in enumerate(messages, 1):
            role = message.get("role", "user")
            content = message.get("content", "")
            
            if role == "user":
                # Mensagem do usuário - simples
                content_clean = content.replace('**', '').replace('*', '').replace('#', '')
                elements.append(Paragraph(
                    f"<b>Pergunta {idx}:</b> {content_clean}",
                    user_style
                ))
            else:
                # Mensagem do assistente - pode conter tabelas
                elements.append(Paragraph(
                    f"<b>Resposta {idx}:</b>",
                    user_style
                ))
                
                # Extrair tabelas Markdown do conteúdo
                tables = extract_markdown_tables(content)
                
                if tables:
                    # Tem tabelas - dividir texto em partes
                    last_pos = 0
                    
                    for table_data, start_pos, end_pos in sorted(tables, key=lambda x: x[1]):
                        # Adicionar texto antes da tabela
                        text_before = content[last_pos:start_pos]
                        if text_before.strip():
                            text_clean = text_before.replace('**', '').replace('*', '').replace('#', '')
                            if len(text_clean) > 2000:
                                text_clean = text_clean[:2000] + "... [truncado]"
                            elements.append(Paragraph(text_clean, assistant_style))
                            elements.append(Spacer(1, 0.2*cm))
                        
                        # Adicionar tabela
                        reportlab_table = create_reportlab_table(table_data)
                        if reportlab_table:
                            elements.append(reportlab_table)
                            elements.append(Spacer(1, 0.3*cm))
                        
                        last_pos = end_pos
                    
                    # Adicionar texto após última tabela
                    text_after = content[last_pos:]
                    if text_after.strip():
                        text_clean = text_after.replace('**', '').replace('*', '').replace('#', '')
                        if len(text_clean) > 2000:
                            text_clean = text_clean[:2000] + "... [truncado]"
                        elements.append(Paragraph(text_clean, assistant_style))
                else:
                    # Sem tabelas - adicionar texto normal
                    content_clean = content.replace('**', '').replace('*', '').replace('#', '')
                    if len(content_clean) > 2000:
                        content_clean = content_clean[:2000] + "... [conteúdo truncado]"
                    elements.append(Paragraph(content_clean, assistant_style))
                
                # Adicionar gráfico se existir
                chart_fig = message.get("chart_fig")
                if chart_fig:
                    try:
                        # Salvar gráfico Plotly como imagem temporária
                        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp_file:
                            tmp_filename = tmp_file.name
                        
                        # Exportar gráfico Plotly para PNG
                        chart_fig.write_image(tmp_filename, width=800, height=500, scale=2)
                        
                        # Adicionar imagem ao PDF
                        img = Image(tmp_filename, width=14*cm, height=8.75*cm)
                        elements.append(Spacer(1, 0.3*cm))
                        elements.append(img)
                        elements.append(Spacer(1, 0.3*cm))
                        
                        # Limpar arquivo temporário
                        try:
                            os.unlink(tmp_filename)
                        except:
                            pass  # Ignorar erro ao deletar arquivo temp
                    except Exception as e:
                        # Se falhar ao exportar gráfico, apenas continuar
                        elements.append(Paragraph(
                            f"[Gráfico não pôde ser incluído: {str(e)}]",
                            info_style
                        ))
            
            elements.append(Spacer(1, 0.3*cm))
    
    elements.append(PageBreak())
    
    # ===== 4. PERGUNTA SOBRE CONCLUSÕES =====
    # Detectar se há pergunta sobre conclusões/insights/recomendações
    has_conclusion_question = False
    conclusion_q_idx = -1
    
    for idx, message in enumerate(messages):
        if message.get("role") == "user":
            content_lower = message.get("content", "").lower()
            if any(word in content_lower for word in ['conclus', 'insight', 'recomend', 'sugest', 'negócio', 'ações', 'estratégia']):
                has_conclusion_question = True
                conclusion_q_idx = idx
                break
    
    elements.append(Paragraph("4. PERGUNTA SOBRE CONCLUSÕES DO AGENTE", subtitle_style))
    elements.append(Spacer(1, 0.3*cm))
    
    if has_conclusion_question and conclusion_q_idx >= 0:
        # Mostrar a pergunta e resposta sobre conclusões
        user_msg = messages[conclusion_q_idx]
        # Buscar resposta correspondente (próxima mensagem do assistant)
        assistant_msg = None
        if conclusion_q_idx + 1 < len(messages):
            assistant_msg = messages[conclusion_q_idx + 1]
        
        elements.append(Paragraph(
            f"<b>Pergunta:</b> {user_msg.get('content', '')}",
            user_style
        ))
        elements.append(Spacer(1, 0.2*cm))
        
        if assistant_msg:
            content_clean = assistant_msg.get('content', '').replace('**', '').replace('*', '').replace('#', '')
            if len(content_clean) > 3000:
                content_clean = content_clean[:3000] + "... [conteúdo truncado para o PDF]"
            elements.append(Paragraph(
                f"<b>Resposta do ConsultantAgent:</b>",
                user_style
            ))
            elements.append(Paragraph(content_clean, assistant_style))
    else:
        elements.append(Paragraph(
            "Nenhuma pergunta sobre conclusões foi identificada nesta sessão. "
            "Recomenda-se fazer perguntas como: 'Quais são as conclusões desta análise?' "
            "ou 'Que insights e recomendações você pode fornecer?'",
            normal_style
        ))
    
    elements.append(Spacer(1, 0.5*cm))
    elements.append(PageBreak())
    
    # ===== 5. CÓDIGOS FONTE GERADOS =====
    elements.append(Paragraph("5. CÓDIGOS FONTE GERADOS", subtitle_style))
    elements.append(Spacer(1, 0.3*cm))
    
    code_style = ParagraphStyle(
        'CodeStyle',
        parent=styles['Code'],
        fontSize=8,
        leftIndent=10,
        rightIndent=10,
        spaceAfter=10,
        fontName='Courier'
    )
    
    # Coletar códigos gerados durante a sessão
    generated_codes = []
    for message in messages:
        if message.get("role") == "assistant":
            code = message.get("generated_code", "")
            if code and code.strip():
                generated_codes.append(code)
    
    if generated_codes:
        elements.append(Paragraph(
            f"Total de códigos gerados: <b>{len(generated_codes)}</b>",
            info_style
        ))
        elements.append(Spacer(1, 0.3*cm))
        
        for idx, code in enumerate(generated_codes[:5], 1):  # Limitar a 5 códigos
            elements.append(Paragraph(
                f"<b>Código {idx}:</b>",
                user_style
            ))
            elements.append(Spacer(1, 0.1*cm))
            
            # Limitar tamanho do código
            if len(code) > 1500:
                code = code[:1500] + "\n\n# ... [código truncado para o PDF]"
            
            # Adicionar código com formatação
            try:
                # Usar Preformatted para manter formatação do código
                code_lines = code.split('\n')
                for line in code_lines[:30]:  # Máximo 30 linhas por código
                    elements.append(Paragraph(line.replace('<', '&lt;').replace('>', '&gt;'), code_style))
            except:
                elements.append(Paragraph(code.replace('<', '&lt;').replace('>', '&gt;'), code_style))
            
            elements.append(Spacer(1, 0.5*cm))
            
            if idx >= 5:
                elements.append(Paragraph(
                    f"[Mais {len(generated_codes) - 5} código(s) omitido(s) do PDF. "
                    f"Todos os códigos estão disponíveis no histórico da aplicação.]",
                    info_style
                ))
                break
    else:
        elements.append(Paragraph(
            "Nenhum código foi gerado nesta sessão. Os códigos são gerados quando o usuário "
            "solicita explicitamente gráficos, análises programáticas ou exportação de notebooks.",
            normal_style
        ))
    
    elements.append(Spacer(1, 0.5*cm))
    
    # Informações sobre o repositório
    repo_info = """
    <b>Código Fonte Completo:</b><br/><br/>
    Todo o código fonte da aplicação está disponível no repositório GitHub:<br/>
    <b>https://github.com/oalbertocavalcante/ai-challenge-i2a2</b><br/><br/>
    
    <b>Estrutura do Repositório:</b><br/>
    • <b>agents/:</b> Implementação dos 5 agentes especializados<br/>
    • <b>components/:</b> Componentes da interface (UI, geração de notebooks, PDF)<br/>
    • <b>utils/:</b> Utilitários (config, memória, cache, geração de PDF)<br/>
    • <b>app.py:</b> Aplicação principal Streamlit<br/>
    • <b>requirements.txt:</b> Dependências Python<br/>
    • <b>README.md:</b> Documentação completa<br/>
    """
    
    elements.append(Paragraph(repo_info, normal_style))
    elements.append(Spacer(1, 0.5*cm))
    elements.append(PageBreak())
    
    # ===== 6. LINK PARA ACESSAR O AGENTE =====
    elements.append(Paragraph("6. LINK PARA ACESSAR O AGENTE", subtitle_style))
    elements.append(Spacer(1, 0.3*cm))
    
    access_text = """
    <b>Sistema Online em Produção:</b><br/><br/>
    
    O agente de análise de dados está disponível online 24/7 através do Streamlit Cloud:<br/><br/>
    
    <b>🔗 URL: https://ai-challenge-i2a2.streamlit.app/</b><br/><br/>
    
    <b>Como Utilizar:</b><br/>
    1. Acesse o link acima em qualquer navegador<br/>
    2. Faça upload de um arquivo CSV (máximo 500MB)<br/>
    3. Digite suas perguntas no chat<br/>
    4. Receba análises estatísticas, gráficos e insights<br/>
    5. Baixe o relatório completo em PDF<br/><br/>
    
    <b>Repositório GitHub:</b><br/>
    <b>https://github.com/oalbertocavalcante/ai-challenge-i2a2</b><br/><br/>
    
    O repositório contém:<br/>
    • Código fonte completo<br/>
    • Documentação técnica detalhada<br/>
    • Instruções de instalação local<br/>
    • Guia de deploy no Streamlit Cloud<br/>
    • Exemplos de uso e perguntas<br/>
    """
    
    elements.append(Paragraph(access_text, normal_style))
    elements.append(Spacer(1, 1*cm))
    
    # Tabela com informações de acesso
    access_data = [
        ['Sistema Online:', 'https://ai-challenge-i2a2.streamlit.app/'],
        ['Repositório GitHub:', 'https://github.com/oalbertocavalcante/ai-challenge-i2a2'],
        ['Documentação:', 'README.md no repositório'],
        ['Participante:', participant_name],
        ['Dataset Utilizado:', dataset_name or 'N/A'],
    ]
    
    access_table = Table(access_data, colWidths=[4.5*cm, 11.5*cm])
    access_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#1F4788')),
        ('BACKGROUND', (1, 0), (1, -1), colors.HexColor('#E8F4F8')),
        ('TEXTCOLOR', (0, 0), (0, -1), colors.white),
        ('TEXTCOLOR', (1, 0), (1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#1F4788')),
    ]))
    
    elements.append(access_table)
    elements.append(Spacer(1, 1*cm))
    
    # Nota final
    sao_paulo_tz = pytz.timezone('America/Sao_Paulo')
    now_sp = datetime.now(sao_paulo_tz)
    
    final_note = f"""
    <b>Nota Final:</b> Este relatório foi gerado automaticamente pelo sistema de análise de dados 
    desenvolvido para a I2A2 Academy. O sistema está em produção e disponível para uso público.<br/><br/>
    
    <b>Data e Hora de Geração:</b> {now_sp.strftime('%d/%m/%Y às %H:%M:%S')} (Horário de São Paulo)<br/>
    <b>Curso:</b> Agentes Autônomos - I2A2 Academy<br/>
    <b>Participante:</b> {participant_name}
    """
    elements.append(Paragraph(final_note, info_style))
    
    # Construir PDF
    doc.build(elements)
    
    buffer.seek(0)
    return buffer
