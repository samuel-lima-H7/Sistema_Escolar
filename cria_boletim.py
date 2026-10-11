
import os

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

import resgate_de_info


def criar_pdf_boletim(aluno, listas_para_pdf):

    pasta_projeto = os.path.dirname(os.path.abspath(__file__))
    pasta_boletins = os.path.join(pasta_projeto, "boletins")

    os.makedirs(pasta_boletins, exist_ok=True)

    nome_arquivo = os.path.join(
        pasta_boletins,
        f"Boletim_{aluno}.pdf"
    )

    dados_tabela = []

    for linha in listas_para_pdf:
        nova_linha = []

        for item in linha:
            if item is None:
                item = ""
            nova_linha.append(str(item))

        dados_tabela.append(nova_linha)

    if not dados_tabela:
        print("Erro: não existem dados para criar o boletim.")
        return

    quantidade_colunas = 6

    for linha in dados_tabela:
        while len(linha) < quantidade_colunas:
            linha.append("")

        if len(linha) > quantidade_colunas:
            del linha[quantidade_colunas:]

    pdf = SimpleDocTemplate(
        nome_arquivo,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    elementos = []
    estilos = getSampleStyleSheet()

    estilo_titulo = estilos["Title"]
    estilo_titulo.alignment = TA_CENTER

    titulo = Paragraph(
        f"Boletim escolar de: {aluno}",
        estilo_titulo
    )

    elementos.append(titulo)
    elementos.append(Spacer(1, 20))

    tabela = Table(
        dados_tabela,
        colWidths=[100, 75, 75, 75, 75, 60]
    )

    tabela.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
            ("TOPPADDING", (0, 0), (-1, 0), 8),
        ])
    )

    elementos.append(tabela)
    pdf.build(elementos)

    print("\nBoletim criado com sucesso!")
    print(f"Local: {nome_arquivo}")


def executar_geracao_do_boletim():
    # Solicita o aluno e recupera suas notas
    alunos = resgate_de_info.verificações()

    if not alunos:
        print("Nenhum registro encontrado para esse aluno.")
        return

    aluno = alunos[0][0]

    # Gera a tabela com as notas recuperadas
    dados_tabela = resgate_de_info.formação_de_lista_para_dados(alunos)

    # A função de formação deve retornar os dados da tabela
    if not dados_tabela:
        print("Não foi possível preparar os dados do boletim.")
        return

    criar_pdf_boletim(aluno, dados_tabela)


if __name__ == "__main__":
    executar_geracao_do_boletim()
