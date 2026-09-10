import os
import csv
from armazenamento_info import verifica_aluno_exstir, alunos_ja_cadastrados

dados_gerais = list()
materias = ["matemática", "português", "ciências", "geografia", "história", "artes", "educação física"]

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
    dado_materia_escolar = []
    while True:
        try:
            while True:
                materia = str(input("Qual matéria deseja agregar nota?\nMatérias disponíveis: Matemática, Português, Ciências, Geografia, História, Artes, Educação Física\nDigite a matéria que deseja agregar nota: "))
                if materia.strip().lower() in materias:
                    dado_materia_escolar.append(materia)
                    break
                else:
                    print("Texto incorreto, digite novamente, reveja os acentos, as letras, etc.")
            break
        except: 
            print("Valor inválido, digite novamente!")
    return materia

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

def armazenamento_geral():
    lista_geral = []
    quant_matérias_já_cadastradas = 0
    while quant_matérias_já_cadastradas < len(materias):
        continuar = str(input("deseja adicionar notas a mais uma matéria? "))
        if continuar == "não":
            break
        else
            disciplina_escolar_nota = materia_escolar()
            bimestres_escolar_nota = bemestre()
            for i in range(bimestres_escolar_nota):
                nota = int(input(f"Digite a nota do aluno na matéria {disciplina_escolar_nota} no bimestre {i}"))
                quant_matérias_já_cadastradas =+ 1


                    






"""
if __name__ == "__main__":
    sim_ou_não = str(input("Deseja adinionar alguma informação?[sim ou não]: ")[0])
    if sim_ou_não == "s":
        
    else:
        print("")
"""