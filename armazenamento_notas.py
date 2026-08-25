import os
import csv
from armazenamento_info import verifica_aluno_exstir, alunos_ja_cadastrados

def bimestre():
    while True:
        try:
            while True:
                quantidade_bimestres = int(input("Quais bimestres deseja agregar nota? \nDigite apenas números: ").strip())
                if quantidade_bimestres > 4:
                    print("""valor inválido, digite novamente!! 
                    """)
                else: 
                    break
            break
        except:
            print("""valor inválido, digite novamente!!
            """)
    return quantidade_bimestres

def materia_escolar():
    materia = str(input("Qual matéria deseja agregar nota?\nMatérias disponíveis: Matemática, Português, Ciências, Geografia, História, Artes, Educação Física\nDigite a matéria que deseja agregar nota: "))

def alunos_agregar_nota():
    while True:
        try:
            while True:
                quant = int(input("Digite a quantidade de alunos nos quais deseja agregar nota: "))
                if quant > len(alunos_ja_cadastrados()):
                    print("quantidade de alunos inexistentes!")
                else:
                    break
            break
        except:
            print("valor inválido, digite novamente!")
    return quant

alunos_agregar_nota()

