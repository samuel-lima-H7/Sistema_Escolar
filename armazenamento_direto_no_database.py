
from armazenamento_info_em_database import gerar_lista_para_csv, polimento_de_dados, lista_geral

import csv
import os


nomes_para_retirada = list()
dados_pre_existentes = list()
dados_polidos = list()
dados_sem_nessecidade_de_alteração = list()

lista_para_cada_linha = gerar_lista_para_csv(lista_geral)


with open("data_base.csv", "r", newline="", encoding="utf-8") as leitura_do_csv:
    leitura_csv = csv.reader(leitura_do_csv, delimiter=";")

    for c in leitura_csv:
        dados_pre_existentes.append(",".join(c))

    for c in dados_pre_existentes:
        dados_polidos.append(c.split(","))


for c in lista_geral:
    nomes_para_retirada.append(c[0])


for indice, valores in enumerate(dados_polidos):

    if valores[0] in nomes_para_retirada:
        continue

    dados_sem_nessecidade_de_alteração.append(valores)



with open("data_base.csv", "w", newline="", encoding="utf-8") as leitura_do_csv:

    adição_csv = csv.writer(leitura_do_csv, delimiter=";")

    for i in dados_sem_nessecidade_de_alteração:
        adição_csv.writerow(i)

    for c in lista_para_cada_linha:
        adição_csv.writerow(c)

