

from armazenamento_info_em_database import gerar_lista_para_csv, lista_geral

import csv
import os


nomes_para_retirada = list()
dados_pre_existentes = list()
dados_polidos = list()
dados_sem_nessecidade_de_alteração = list()

# ALTERADO: removida a execução antecipada desta linha:
# lista_para_cada_linha = gerar_lista_para_csv(lista_geral)
#
# Ela será executada dentro da função, no momento correto.


# ALTERADO: nome compatível com a chamada atualizar_database()
# utilizada no main.py.
def atualizar_database():

    # ALTERADO: limpa as listas auxiliares a cada execução.
    # Isso evita misturar dados de execuções anteriores.
    nomes_para_retirada.clear()
    dados_pre_existentes.clear()
    dados_polidos.clear()
    dados_sem_nessecidade_de_alteração.clear()

    # MANTIDO: lê os dados que já existem no CSV.
    with open("data_base.csv", "r", newline="", encoding="utf-8") as leitura_do_csv:
        leitura_csv = csv.reader(leitura_do_csv, delimiter=";")

        for c in leitura_csv:
            dados_pre_existentes.append(",".join(c))

        for c in dados_pre_existentes:
            dados_polidos.append(c.split(","))

    # MANTIDO: identifica os alunos que serão atualizados.
    for c in lista_geral:
        nomes_para_retirada.append(c[0])

    # MANTIDO: preserva os registros de outros alunos.
    for indice, valores in enumerate(dados_polidos):

        if valores[0] in nomes_para_retirada:
            continue

        dados_sem_nessecidade_de_alteração.append(valores)

    # ALTERADO: gera as linhas somente agora, depois que
    # lista_geral foi preenchida pela função de polimento.
    lista_para_cada_linha = gerar_lista_para_csv(lista_geral)

    # MANTIDO: regrava o CSV com os dados preservados
    # e com as novas linhas geradas.
    with open("data_base.csv", "w", newline="", encoding="utf-8") as leitura_do_csv:

        adição_csv = csv.writer(leitura_do_csv, delimiter=";")

        for i in dados_sem_nessecidade_de_alteração:
            adição_csv.writerow(i)

        for c in lista_para_cada_linha:
            adição_csv.writerow(c)

