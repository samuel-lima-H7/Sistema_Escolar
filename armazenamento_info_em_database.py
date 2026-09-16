import os
import csv

dados_do_csv = []
dados = [ ['bartolomeu', {'matemática': [1, 2, 3]}], ['bartolomeu', {'geografia':[1, 2, 3]}], ['samuel', {'matemática': [1, 2, 3]}], ['samuel', {'geografia': [1, 2, 3]}],]

alunos_do_csv = 0
with open("data_base.csv", "r", newline="", encoding="utf-8") as f:
    objeto_csv_leitura  = csv.reader(f, delimiter = ";")
    for c in range(len(dados)):
        aluno = dados[c][0]
        print(aluno)
        for valor in objeto_csv_leitura:
            print(valor)
            alunos_do_csv = valor[0]
            if alunos_do_csv == "Alunos":
                continue

            if alunos_do_csv == aluno:
                dados_do_csv.append(valor)


'''
for cont in dados_do_csv:
    for mat in
'''
    

