"""
Gerador de Relatório em PDF
Gera relatório técnico completo da análise de dados
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from datetime import datetime
import io

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
    elements.append(Paragraph("RELATÓRIO TÉCNICO", title_style))
    elements.append(Spacer(1, 0.5*cm))
    elements.append(Paragraph("Relatório da Atividade Extra:", subtitle_style))
    elements.append(Paragraph("Agentes Autônomos de Análise de Dados", subtitle_style))
    elements.append(Spacer(1, 2*cm))
    
    # Tabela de informações
    data = [
        ['Participante:', participant_name],
        ['Dataset Analisado:', dataset_name or 'N/A'],
        ['Data de Geração:', datetime.now().strftime('%d/%m/%Y %H:%M:%S')],
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
    
    # ===== SUMÁRIO EXECUTIVO =====
    elements.append(Paragraph("1. SUMÁRIO EXECUTIVO", subtitle_style))
    elements.append(Spacer(1, 0.3*cm))
    
    summary_text = f"""
    Este relatório apresenta a análise exploratória de dados realizada através de um sistema 
    de agentes autônomos baseados em IA. O sistema utiliza 5 agentes especializados 
    (CoordinatorAgent, DataAnalystAgent, VisualizationAgent, ConsultantAgent e CodeGeneratorAgent) 
    para processar e analisar o dataset "{dataset_name or 'fornecido'}".
    <br/><br/>
    O sistema implementa memória contextual completa, permitindo que os agentes acessem 
    análises anteriores para gerar conclusões fundamentadas e insights de negócio acionáveis.
    """
    
    elements.append(Paragraph(summary_text, normal_style))
    elements.append(Spacer(1, 0.5*cm))
    
    # ===== HISTÓRICO DA CONVERSA =====
    elements.append(Paragraph("2. HISTÓRICO DA ANÁLISE", subtitle_style))
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
            
            # Limpar conteúdo para PDF (remover markdown complexo)
            content_clean = content.replace('**', '').replace('*', '').replace('#', '')
            
            if role == "user":
                elements.append(Paragraph(
                    f"<b>Pergunta {idx}:</b> {content_clean}",
                    user_style
                ))
            else:
                # Limitar tamanho da resposta se muito grande
                if len(content_clean) > 2000:
                    content_clean = content_clean[:2000] + "... [conteúdo truncado]"
                
                elements.append(Paragraph(
                    f"<b>Resposta {idx}:</b>",
                    user_style
                ))
                elements.append(Paragraph(content_clean, assistant_style))
            
            elements.append(Spacer(1, 0.3*cm))
    
    elements.append(PageBreak())
    
    # ===== CONCLUSÕES =====
    elements.append(Paragraph("3. ARQUITETURA DO SISTEMA", subtitle_style))
    elements.append(Spacer(1, 0.3*cm))
    
    architecture_text = """
    <b>3.1 Agentes Especializados</b><br/><br/>
    
    <b>• CoordinatorAgent:</b> Responsável pelo roteamento inteligente de perguntas para o agente 
    mais adequado. Analisa a intenção do usuário e direciona para análise estatística, 
    visualização, insights ou geração de código.<br/><br/>
    
    <b>• DataAnalystAgent:</b> Especializado em análises estatísticas descritivas, incluindo 
    cálculo de médias, medianas, desvios padrão, correlações, detecção de outliers e 
    identificação de padrões nos dados.<br/><br/>
    
    <b>• VisualizationAgent:</b> Gera código Python para criação de gráficos interativos usando 
    Plotly, incluindo histogramas, scatter plots, box plots, heatmaps e gráficos de linha.<br/><br/>
    
    <b>• ConsultantAgent:</b> Fornece insights de negócio, conclusões baseadas em evidências e 
    recomendações estratégicas. Utiliza toda a memória de análises anteriores para gerar 
    conclusões fundamentadas.<br/><br/>
    
    <b>• CodeGeneratorAgent:</b> Gera código Python completo e exportável em formato Jupyter 
    Notebook para reprodução das análises.<br/><br/>
    
    <b>3.2 Implementação de Memória</b><br/><br/>
    
    O sistema implementa memória contextual através de <b>st.session_state.all_analyses_history</b>, 
    que armazena todas as análises realizadas durante a sessão. Esta memória é passada para 
    todos os agentes, permitindo:<br/>
    - Respostas contextualizadas baseadas em análises anteriores<br/>
    - Geração de conclusões fundamentadas em múltiplas análises<br/>
    - Recomendações estratégicas baseadas em padrões identificados<br/>
    - Continuidade da conversa com contexto completo<br/><br/>
    
    <b>3.3 Tecnologias Utilizadas</b><br/><br/>
    
    • <b>Framework de IA:</b> LangChain + Google Gemini 1.5 Flash<br/>
    • <b>Interface:</b> Streamlit<br/>
    • <b>Análise de Dados:</b> Pandas, NumPy, Scikit-learn<br/>
    • <b>Visualização:</b> Plotly, Seaborn<br/>
    • <b>Versionamento:</b> Git + GitHub<br/>
    • <b>Deploy:</b> Streamlit Cloud<br/>
    """
    
    elements.append(Paragraph(architecture_text, normal_style))
    
    elements.append(PageBreak())
    
    # ===== RODAPÉ =====
    elements.append(Paragraph("4. INFORMAÇÕES DE ACESSO", subtitle_style))
    elements.append(Spacer(1, 0.3*cm))
    
    access_data = [
        ['Repositório GitHub:', 'https://github.com/oalbertocavalcante/ai-challenge-i2a2'],
        ['Sistema Online:', 'https://ai-challenge-i2a2.streamlit.app/'],
        ['Documentação:', 'README.md no repositório'],
        ['Licença:', 'MIT License'],
    ]
    
    access_table = Table(access_data, colWidths=[4*cm, 12*cm])
    access_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#E8F4F8')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ]))
    
    elements.append(access_table)
    elements.append(Spacer(1, 1*cm))
    
    # Nota final
    final_note = """
    <b>Nota:</b> Este relatório foi gerado automaticamente pelo sistema de análise de dados. 
    Para reproduzir as análises, acesse o repositório GitHub e siga as instruções do README.md.
    """
    elements.append(Paragraph(final_note, info_style))
    
    elements.append(Spacer(1, 1*cm))
    elements.append(Paragraph(
        f"Relatório gerado em: {datetime.now().strftime('%d/%m/%Y às %H:%M:%S')}",
        info_style
    ))
    
    # Construir PDF
    doc.build(elements)
    
    buffer.seek(0)
    return buffer
