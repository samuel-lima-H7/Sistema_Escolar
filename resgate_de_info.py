import os 
import csv
from armazenamento_info import alunos_ja_cadastrados
alunos_disponiveis = alunos_ja_cadastrados()
alunos_para_boletim = []
listas_para_pdf = []
materias = {"matemática":1, "português":2, "ciências":3, "geografia":4, "história":5, "artes":6, "educação física":7}


def formação_de_lista_para_dados(alunos):
    indice_para_cada_bimestre = 1
    lista_para_linha = []
    for key, value in materias.items():
        lista_para_linha = [key]
        for c in alunos:
            lista_para_linha.append(c[value])

        listas_para_pdf.append(lista_para_linha)

    for linha in listas_para_pdf:

        notas = []

        for nota in linha[1:]:
            if nota == "":
                notas.append(0)
            else:
                notas.append(int(nota))

        total = sum(notas)

        linha.append(total)
    
    listas_para_pdf.insert(0,["Matérias", "1º Bimestre", "2º Bimestre", "3º Bimestre", "4º Bimestre", "Total"])

while True:
    try:
        while True:
            aluno = str(input("Digite o nome do aluno que deseja o boletim: "))
            if aluno in alunos_disponiveis:
                break
            else:
                print("Digite novamente, valor inválido")
        break
    except:
        print("Digite novamente, valor inválido")


with open("data_base.csv", "r", newline="") as objeto_de_leitura:
    objeto_csv = csv.reader(objeto_de_leitura, delimiter=";")
    for c in objeto_csv:
        if c[0] != aluno:
            continue
        else:
            alunos_para_boletim.append(c)

formação_de_lista_para_dados(alunos_para_boletim)
        

    