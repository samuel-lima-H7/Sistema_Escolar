import os
import csv
dados = list()

def info_aluno(aluno):
    with open("data_base.csv", "a", newline="", encoding="utf-8") as armazena:
        armazena_csv = csv.writer(armazena, delimiter=";")
        for c in range(4):
            armazena_csv.writerow([aluno, "", "", "", "", "", "", ""])


def alunos_ja_cadastrados():
    alunos =  list()
    with open("data_base.csv", "r", newline="", encoding="utf-8") as verifica:
        verifica_csv = csv.reader(verifica, delimiter=";")
        for cont, valor in enumerate(verifica_csv):
            if cont == 0 or not valor:
                continue
            dados.append(",".join(valor))
    filtro = dados[0::4]

    for valor_da_linha in filtro:
        nome = valor_da_linha.split(",") 
        alunos.append(nome[0])

    return alunos

def verifica_aluno_exstir(alunos_recebido, alunos_existentes):
    retorno = ""
    if alunos_recebido in alunos_existentes:
        retorno =  "aluno já presente em banco de dados"
    else:
        retorno = "aluno não identificado no banco de dados, pode ser adicionado"

    return retorno
    

nome_para_verificar_ou_cadastrar =  input(str("Qual aluno deseja cadastrar?: "))
print(verifica_aluno_exstir(nome_para_verificar_ou_cadastrar, alunos_ja_cadastrados()))

