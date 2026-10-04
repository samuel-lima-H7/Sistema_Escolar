from resgate_de_info import aluno, listas_para_pdf

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer
)

import os


def criar_pdf_boletim(aluno, listas_para_pdf):

    # ==========================================================
    # 1. LOCAL DA PASTA DOS BOLETINS
    # ==========================================================

    pasta_projeto = os.path.dirname(os.path.abspath(__file__))

    pasta_boletins = os.path.join(
        pasta_projeto,
        "boletins"
    )

    # Cria a pasta caso ela não exista
    os.makedirs(pasta_boletins, exist_ok=True)


    # ==========================================================
    # 2. NOME DO ARQUIVO
    # ==========================================================

    nome_arquivo = os.path.join(
        pasta_boletins,
        f"Boletim_{aluno}.pdf"
    )


    # ==========================================================
    # 3. PREPARAÇÃO DOS DADOS DA TABELA
    # ==========================================================

    dados_tabela = []

    for linha in listas_para_pdf:

        # Verifica se a linha realmente é uma lista
        if not isinstance(linha, list):
            linha = [linha]

        nova_linha = []

        for item in linha:

            # Converte todos os valores para texto
            # Isso evita problemas com o ReportLab
            if item is None:
                item = ""

            else:
                item = str(item)

            nova_linha.append(item)

        dados_tabela.append(nova_linha)


    # ==========================================================
    # 4. VERIFICAÇÃO DA TABELA
    # ==========================================================

    if not dados_tabela:
        print("Erro: não existem dados para criar o boletim.")
        return


    # Todas as linhas precisam ter 6 colunas
    quantidade_colunas = 6

    for linha in dados_tabela:

        while len(linha) < quantidade_colunas:
            linha.append("")

        if len(linha) > quantidade_colunas:
            del linha[quantidade_colunas:]


    # ==========================================================
    # 5. CRIAÇÃO DO PDF
    # ==========================================================

    pdf = SimpleDocTemplate(
        nome_arquivo,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )


    elementos = []


    # ==========================================================
    # 6. TÍTULO
    # ==========================================================

    estilos = getSampleStyleSheet()

    estilo_titulo = estilos["Title"]
    estilo_titulo.alignment = TA_CENTER

    titulo = Paragraph(
        f"Boletim escolar de: {aluno}",
        estilo_titulo
    )

    elementos.append(titulo)

    elementos.append(
        Spacer(1, 20)
    )


    # ==========================================================
    # 7. CRIAÇÃO DA TABELA
    # ==========================================================

    tabela = Table(
        dados_tabela,
        colWidths=[
            100,
            75,
            75,
            75,
            75,
            60
        ]
    )


    # ==========================================================
    # 8. FORMATAÇÃO DA TABELA
    # ==========================================================

    tabela.setStyle(
        TableStyle([

            # Cabeçalho
            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.grey
            ),

            (
                "TEXTCOLOR",
                (0, 0),
                (-1, 0),
                colors.white
            ),

            (
                "FONTNAME",
                (0, 0),
                (-1, 0),
                "Helvetica-Bold"
            ),

            # Alinhamento
            (
                "ALIGN",
                (0, 0),
                (-1, -1),
                "CENTER"
            ),

            (
                "VALIGN",
                (0, 0),
                (-1, -1),
                "MIDDLE"
            ),

            # Linhas da tabela
            (
                "GRID",
                (0, 0),
                (-1, -1),
                1,
                colors.black
            ),

            # Espaçamento
            (
                "BOTTOMPADDING",
                (0, 0),
                (-1, 0),
                8
            ),

            (
                "TOPPADDING",
                (0, 0),
                (-1, 0),
                8
            ),

        ])
    )


    elementos.append(tabela)


    # ==========================================================
    # 9. GERAÇÃO DO PDF
    # ==========================================================

    pdf.build(elementos)


    print(
        f"\nBoletim criado com sucesso!"
    )

    print(
        f"Local: {nome_arquivo}"
    )


# ==============================================================
# EXECUTA A CRIAÇÃO DO BOLETIM
# ==============================================================

criar_pdf_boletim(
    aluno,
    listas_para_pdf
)