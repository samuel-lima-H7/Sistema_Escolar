import os
import csv
from armazenamento_info import verifica_aluno_exstir, alunos_ja_cadastrados


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


materia_escolar()