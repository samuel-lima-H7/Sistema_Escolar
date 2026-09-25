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




def gerar_lista_para_csv(dados_gerais):
    lista_para_cada_linha = []
    indice_para_cada_materia = 0

    for cont in dados_gerais:
        linha_csv = [cont[0], "", "", "", "", "", "", "", ""]
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
            
            for nota in value:
                if indice_para_cada_materia == 1:
                    del linha_csv[1]
                    linha_csv.insert(1, f"{nota}")
                    lista_para_cada_linha.append(linha_csv)

                elif indice_para_cada_materia == 2:
                    del linha_csv[2]
                    linha_csv.insert(2, f"{nota}")
                    lista_para_cada_linha.append(linha_csv)
                    
                elif  indice_para_cada_materia == 3:
                    del linha_csv[3]
                    linha_csv.insert(3, f"{nota}")
                    lista_para_cada_linha.append(linha_csv)

                elif indice_para_cada_materia == 4:
                    del linha_csv[4]
                    linha_csv.insert(4, f"{nota}")
                    lista_para_cada_linha.append(linha_csv)

                elif indice_para_cada_materia == 5:
                    del linha_csv[5]
                    linha_csv.insert(5, f"{nota}")
                    lista_para_cada_linha.append(linha_csv)

                elif indice_para_cada_materia == 6:
                    del linha_csv[6]
                    linha_csv.insert(6, f"{nota}")
                    lista_para_cada_linha.append(linha_csv)

                elif indice_para_cada_materia == 7:
                    del linha_csv[7]
                    linha_csv.insert(7, f"{nota}")
                    lista_para_cada_linha.append(linha_csv)

                lista_para_cada_linha.append(linha_csv.copy())

    linha.append(lista_para_cada_linha)


gerar_lista_para_csv(lista_geral)

for c in linha:
    print(f"{c}",end="")
    print("")
