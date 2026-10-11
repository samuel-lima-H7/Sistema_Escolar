

# FUNÇÃO NÚMERO 1
import armazenamento_info

# FUNÇÃO NÚMERO 2
import armazenamento_notas
import armazenamento_info_em_database
import armazenamento_direto_no_database

# FUNÇÃO NÚMERO 3
import resgate_de_info
import cria_boletim


def função_que_executa_outras_funções(número):

    if número == 1:
        armazenamento_info.armazena()

    elif número == 2:
        # ALTERADO: primeiro coleta as notas.
        armazenamento_notas.retorna_lista_geral_com_materias()

        # ALTERADO: depois organiza os dados coletados.
        armazenamento_info_em_database.polimento_de_dados()

        # ALTERADO: por último, atualiza o CSV.
        armazenamento_direto_no_database.atualizar_database()

    elif número == 3:
        cria_boletim.executar_geracao_do_boletim()


# ALTERADO: o menu inteiro fica dentro de um único while.
# Assim, o programa continua funcionando até a opção 0.
while True:
    try:
        print("[1] - Cadastrar aluno no banco de dados")
        print("[2] - Cadastrar notas dos alunos")
        print("[3] - Gerar boletim do aluno")
        print("[0] - Encerrar o programa")

        function = int(
            input("Digite o número da função que deseja executar: ")
        )

        if function == 0:
            print("Programa encerrado.")
            break

        elif 1 <= function <= 3:
            # ALTERADO: agora a opção escolhida é executada.
            função_que_executa_outras_funções(function)

        else:
            print("Valor inválido, digite novamente.")

    except ValueError:
        print("Valor inválido, digite um número.")
