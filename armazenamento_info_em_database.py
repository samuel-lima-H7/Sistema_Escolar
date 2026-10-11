
from armazenamento_notas import dados_gerais


linha = []
lista_geral = []
lista_para_armazenar_no_csv = []


def polimento_de_dados():
    # ALTERADO: limpa os resultados anteriores antes de processar
    # os dados novos. Evita duplicações ao executar novamente.
    lista_geral.clear()

    materias_por_aluno = {}

    # MANTIDO: agrupa as matérias pelo nome de cada aluno.
    for item in dados_gerais:
        nome = item[0]
        materia_dict = item[1]

        if nome not in materias_por_aluno:
            materias_por_aluno[nome] = {}

        materias_por_aluno[nome].update(materia_dict)

    # MANTIDO: completa cada matéria até quatro bimestres.
    for nome, dicionario_materias in materias_por_aluno.items():

        for materia, notas in dicionario_materias.items():
            while len(notas) < 4:
                notas.append("")

        linha_aluno = [nome, dicionario_materias]

        lista_geral.append(linha_aluno)

    # MANTIDO: retorna a lista já processada.
    # O retorno é útil caso outra parte do programa precise recebê-la.
    return lista_geral


# ALTERADO: removida a chamada automática:
# polimento_de_dados()
#
# A função agora será chamada pelo main.py, depois que
# o usuário cadastrar as notas.


def gerar_lista_para_csv(dados_gerais):
    lista_para_cada_linha = []
    indice_para_cada_materia = 0

    # MANTIDO: percorre cada aluno e suas matérias.
    for cont in dados_gerais:

        nome_vingente = cont[0]
        linhas_do_aluno = []

        for key, value in cont[1].items():

            if key == "matemática":
                indice_para_cada_materia = 1

            elif key == "português":
                indice_para_cada_materia = 2

            elif key == "ciências":
                indice_para_cada_materia = 3

            elif key == "geografia":
                indice_para_cada_materia = 4

            elif key == "história":
                indice_para_cada_materia = 5

            elif key == "artes":
                indice_para_cada_materia = 6

            elif key == "educação física":
                indice_para_cada_materia = 7

            # MANTIDO: cada índice representa um bimestre.
            for indice_bimestre, nota in enumerate(value):

                if indice_bimestre < len(linhas_do_aluno):

                    # MANTIDO: reutiliza a linha do bimestre existente.
                    linha_csv = linhas_do_aluno[indice_bimestre]

                    # MANTIDO: preenche a coluna da matéria.
                    linha_csv[indice_para_cada_materia] = str(nota)

                else:

                    # MANTIDO: cria uma linha para o bimestre
                    # quando ela ainda não existe.
                    linha_csv = [
                        nome_vingente, "", "", "",
                        "", "", "", ""
                    ]

                    linha_csv[indice_para_cada_materia] = str(nota)

                    lista_para_cada_linha.append(linha_csv)
                    linhas_do_aluno.append(linha_csv)

    # MANTIDO: devolve as linhas preparadas para o CSV.
    return lista_para_cada_linha



'''

VERSÃO ANTIGA DA ESTRUTURA

def gerar_lista_para_csv(dados_gerais):
    lista_para_cada_linha = []
    indice_para_cada_materia = 0

    for cont in dados_gerais:
        for key, value in cont[1].items():
            nome_vingente = cont[0]
            if key == "matemática":
                indice_para_cada_materia = 1

            elif key == "português":
                indice_para_cada_materia = 2
                
            elif key == "ciências":
                indice_para_cada_materia = 3

            elif key == "geografia":
                indice_para_cada_materia = 4

            elif key == "história":
                indice_para_cada_materia = 5

            elif key == "artes":
                indice_para_cada_materia = 6

            elif key == "educação física":
                indice_para_cada_materia = 7
            
            if nome_vingente == lista_para_cada_linha[]
            
            for nota in value:
                linha_csv = [cont[0], "", "", "", "", "", "", "", ""]
                if indice_para_cada_materia == 1:
                    linha_csv[indice_para_cada_materia] = str(nota)
                    lista_para_cada_linha.append(linha_csv)

                elif indice_para_cada_materia == 2:
                    linha_csv[indice_para_cada_materia] = str(nota)
                    lista_para_cada_linha.append(linha_csv)

                elif  indice_para_cada_materia == 3:
                    linha_csv[indice_para_cada_materia] = str(nota)
                    lista_para_cada_linha.append(linha_csv)

                elif indice_para_cada_materia == 4:
                    linha_csv[indice_para_cada_materia] = str(nota)
                    lista_para_cada_linha.append(linha_csv)


                elif indice_para_cada_materia == 5:
                    linha_csv[indice_para_cada_materia] = str(nota)
                    lista_para_cada_linha.append(linha_csv)

                elif indice_para_cada_materia == 6:
                    linha_csv[indice_para_cada_materia] = str(nota)
                    lista_para_cada_linha.append(linha_csv)


                elif indice_para_cada_materia == 7:
                    linha_csv[indice_para_cada_materia] = str(nota)
                    lista_para_cada_linha.append(linha_csv)

                lista_para_cada_linha.append(linha_csv)

    return lista_para_cada_linha
'''


