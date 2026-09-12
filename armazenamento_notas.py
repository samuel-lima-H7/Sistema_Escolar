import os
import csv
from armazenamento_info import verifica_aluno_exstir, alunos_ja_cadastrados


dados_gerais = []
materias = ["matemática", "português", "ciências", "geografia", "história", "artes", "educação física"]

def bimestre():
    while True:
        try:
            while True:
                quantidade_bimestres = int(input("\nQuais bimestres deseja agregar nota? \nDigite apenas números: ").strip())
                if quantidade_bimestres > 4:
                    print("""\nValor inválido, digite novamente!! 
                    """)
                else: 
                    break
            break
        except:
            print("""\nValor inválido, digite novamente!!
            """)
    return quantidade_bimestres

def materia_escolar():
    dado_materia_escolar = []
    while True:
        try:
            while True:
                print("=-"*30)
                materia = str(input("\nQual matéria deseja agregar nota?\n\nMatérias disponíveis: Matemática, Português, Ciências, Geografia, História, Artes, Educação Física\n\nDigite a matéria que deseja agregar nota: "))
                if materia.strip().lower() in materias:
                    dado_materia_escolar.append(materia)
                    break
                else:
                    print("\nTexto incorreto, digite novamente, reveja os acentos, as letras, etc.")
            break
        except: 
            print("\nValor inválido, digite novamente!")
    return materia

def alunos_agregar_nota():
    while True:
        try:
            while True:
                print("=-"*30)
                quant = int(input("\nDigite a quantidade de alunos nos quais deseja agregar nota: "))
                if quant > len(alunos_ja_cadastrados()):
                    print("\nQuantidade de alunos inexistentes!")
                else:
                    break
            break
        except:
            print("\nValor inválido, digite novamente!")
    return quant

def armazenamento_geral(nome_do_aluno):
    quant_matérias_já_cadastradas = 0

    while quant_matérias_já_cadastradas < len(materias):

        continuar = str(input("\nDeseja continuar?: "))
        if continuar.strip().lower()[0] == "s":
            lista_do_aluno = []
            nota_para_cada_materia = []
            dicionário_para_cada_matéria = {}

        
            disciplina_escolar_nota = materia_escolar()
            bimestres_escolar_nota = bimestre()

            for i in range(bimestres_escolar_nota):
                while True:
                    try:
                        nota = int(input(f"\nDigite a nota do aluno na matéria {disciplina_escolar_nota} no bimestre {i+1}: "))
                        nota_para_cada_materia.append(nota)
                        break
                    except:
                        print("\nValor inválido, digite novamente")

            dicionário_para_cada_matéria[f"{disciplina_escolar_nota}"] = nota_para_cada_materia
            lista_do_aluno.append(dicionário_para_cada_matéria)
            lista_do_aluno.insert(0, nome_do_aluno)
            dados_gerais.append(lista_do_aluno)
            quant_matérias_já_cadastradas =+ 1

        elif continuar.strip().lower()[0] == "n":
            break
            
        else:
            print("\nDigite uma valor válido")

    


def retorna_lista_geral_com_materias():
    lista_dos_alunos_a_serem_armazenadas = []
    print("=-"*30)
    print("\nOs alunos disponíveis para cadastro de notas:  \n")
    for i in alunos_ja_cadastrados():
        print(i.capitalize())
    print("")
    numero_de_alunos = alunos_agregar_nota()
    for quantidade in range(numero_de_alunos):
        while True:
            try:
                while True:
                    print("=-"*30)
                    student = str(input("Qual desses alunos deseja cadastrar?: "))
                    if student.strip().lower() in alunos_ja_cadastrados():
                        break
                    else:
                        print("\nAluno não disponível! ")

                break
            except:
                print("\nValor inválido, digite novamente!!!")
        
        armazenamento_geral(student)


retorna_lista_geral_com_materias()
        
print(dados_gerais)