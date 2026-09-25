linha = []
lista_geral = []
lista_para_armazenar_no_csv = []


dados = [ ['bartolomeu', {'matemática': [1, 2, 3]}], ['bartolomeu', {'geografia': [1, 2, 3]}], ['samuel', {'matemática': [1, 2, 3]}], ['samuel', {'geografia': [1, 2, 3]}]]

def polimento_de_dados():
    materias_por_aluno = {}
    
    for item in dados:
        nome = item[0]
        materia_dict = item[1]
        
        if nome not in materias_por_aluno:
            materias_por_aluno[nome] = {}
            

        materias_por_aluno[nome].update(materia_dict)


    for nome, dicionario_materias in materias_por_aluno.items():
        linha_aluno = [nome, dicionario_materias]
        
        lista_geral.append(linha_aluno)

polimento_de_dados()

print(lista_geral)


def gerar_lista_para_csv(dados_gerais):
    lista_para_cada_linha = []
    indice_para_cada_materia = 0

    for cont in dados_gerais:

        nome_vingente = cont[0]

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

            for indice_bimestre, nota in enumerate(value):

                # Verifica se já existe uma linha desse aluno
                if indice_bimestre < len(lista_para_cada_linha):

                    # Pega a linha correspondente ao bimestre
                    linha_csv = lista_para_cada_linha[indice_bimestre]

                    # Verifica se é o mesmo aluno
                    if linha_csv[0] == nome_vingente:

                        # Apenas adiciona a nova matéria
                        linha_csv[indice_para_cada_materia] = str(nota)

                    else:

                        linha_csv = [nome_vingente, "", "", "", "", "", "", ""]

                        linha_csv[indice_para_cada_materia] = str(nota)

                        lista_para_cada_linha.append(linha_csv)

                else:

                    linha_csv = [nome_vingente, "", "", "", "", "", "", ""]

                    linha_csv[indice_para_cada_materia] = str(nota)

                    lista_para_cada_linha.append(linha_csv)

    return lista_para_cada_linha

print(gerar_lista_para_csv(lista_geral))



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


