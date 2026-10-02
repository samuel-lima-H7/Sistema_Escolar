from armazenamento_info_em_database import gerar_lista_para_csv, polimento_de_dados, lista_geral

import csv
import os




nomes_para_retirada = list()
dados_pre_existentes = list()
dados_polidos = list()
dados_sem_nessecidade_de_alteração = list()
with open("data_base.csv", "r", newline="", encoding="utf-8") as leitura_do_csv:
    leitura_csv = csv.reader(leitura_do_csv, delimiter = ";")
    for c in leitura_csv:
        dados_pre_existentes.append(",".join(c))
    for c in dados_pre_existentes:
        dados_polidos.append(c.split(","))

for c in lista_geral:
    nomes_para_retirada.append(c[0])


for indice, valores in enumerate(dados_polidos):
    if indice == 0:
        continue
    if valores[0] in nomes_para_retirada:
        continue
    dados_sem_nessecidade_de_alteração.append(valores)

print(dados_sem_nessecidade_de_alteração)