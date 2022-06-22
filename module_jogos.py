import csv
import os
import pandas as pd


def jogo():
    def menu(ops):
        print("-" * 30)
        for op in ops:
            print(op)
        print("-" * 30)
        op = int(input("Qual opção deseja escolher: "))
        return op

    def cadastrar_jogo():
        jogo = {}

        nome = input("Digite seu nome: ")
        ano = input("Digite seu ano: ")
        categoria = input("Digite sua categoria: ")

        # buscar cliente cadastrado através de ano
        jogo[ano] = [nome, categoria]

        colunas = ['ano', 'nome', 'categoria']  # colunas da tabela .csv
        file_exists = os.path.isfile('jogo.csv')
        with open('jogo.csv', 'a', newline='') as jogo_csv:
            # DictWriter grava dados no formato de dicionário
            cadastrar = csv.DictWriter(
                jogo_csv, fieldnames=colunas, delimiter=',', lineterminator='\r\n')  # fieldnames = nome de campos, ou seja -> colunas, divisor de dados sendo ',', lineterminator \r\n serve para quebrar a linha
            # caso não existe o arquivo 'file_exist', faz o fieldnames funcionar, visto que há o 'writeheader()'
            if not file_exists:
                # writeheader grava a primeira linha de arquivo csv usando os nomes de campo pré-especificados.
                cadastrar.writeheader()
            # escrever nas linhas em respectivas 'keys' e 'values', title() -> deixar letra maiuscula
            cadastrar.writerow(
                {'ano': ano, 'nome': nome.title(), 'categoria': categoria})

        print('Cadastro realizado com sucesso!')
        return jogo
        

    def editar_jogo(jogo):
        alguem = pesquisar_jogo(jogo)
        if alguem == None:
            print("jogo não localizada.")
            op = input("Gostaria de cadastrá-la? (s/n)")
            if op == "s":
                return cadastrar_jogo()
            else:
                return None
        else:
            for i in range(len(jogo) - 1):
                if jogo[i] == alguem:
                    del(jogo[i])
            cadastrar_jogo()

    def excluir_jogo(jogo):
        alone = pesquisar_jogo(jogo)
        if alone == None:
            print("jogo não localizadas.")
        else:
            # excluindo jogo
            for i in range(len(jogo) - 1):  # para i dentro da lista jogo
                if jogo[i] == alone:
                    del(jogo[i])

    def pesquisar_jogo(jogo):
        nome = input("Qual jogo deseja localizar? (Digite o nome)")
        for jogo in jogo:
            if jogo["nome"] == nome:
                return jogo
        return None

    def listar_jogo():
        url = './jogo.csv'
        df = pd.read_csv(url)

        print(df)

    def realizar_emprestimo():
        print('\n------ EMPRÉSTIMOS ------\n')
        cpf = input("Digite o cpf do cliente: ")
        with open('clientes.csv') as clientes_csv:
            reader_obj = csv.reader(clientes_csv, delimiter=',')

            linhas = 0
            for coluna in reader_obj:
                if linhas == 0:
                    linhas += 1
                else:
                    if coluna[0] == cpf:
                        pesquisado = coluna[1]
                        print(f"cpf: {pesquisado} | idade: {coluna[2]}")
                        codigo_jogo = input("Digite seu codigo_jogo: ")
                        data = input("Digite a data do jogo: ")

                        colunas = ['codigo do jogo', 'cpf', 'nome', 'data']  # colunas da tabela .csv
                        file_exists = os.path.isfile('emprestimo.csv')
                        with open('emprestimo.csv', 'a', newline='') as emprestimo_csv:
                            # DictWriter grava dados no formato de dicionário
                            cadastrar = csv.DictWriter(
                                emprestimo_csv, fieldnames=colunas, delimiter=',', lineterminator='\r\n')  # fieldnames = cpf de campos, ou seja -> colunas, divisor de dados sendo ';', lineterminator \r\n serve para quebrar a linha
                            # caso não existe o arquivo 'file_exist', faz o fieldnames funcionar, visto que há o 'writeheader()'
                            if not file_exists:
                                # writeheader grava a primeira linha de arquivo csv usando os cpfs de campo pré-especificados.
                                cadastrar.writeheader()
                            # escrever nas linhas em respectivas 'keys' e 'values', title() -> deixar letra maiuscula
                            cadastrar.writerow(
                                {'codigo do jogo': codigo_jogo, 'cpf': cpf, 'nome': pesquisado ,'data': data})

                        print('Cadastro realizado com sucesso!')
                        return pesquisado
                    else:
                        linhas += 1
            print("pessoa não localizada")
            return None

        
    
    def listar_emprestimos():
        url = './emprestimo.csv'
        df = pd.read_csv(url)
        print(df)



    def start(ops, jogo):
        while True:
            op = menu(ops)
            if op == 1:
                jogo = cadastrar_jogo()
                jogo.append(jogo)
            elif op == 2:
                jogo = editar_jogo(jogo)
            elif op == 3:
                alone = excluir_jogo(jogo)
            elif op == 4:
                alguem = pesquisar_jogo(jogo)
                if alguem != None:
                    print(alguem)
            elif op == 5:
                listar_jogo()
            elif op == 6:
                realizar_emprestimo()
            elif op == 7:
                listar_emprestimos()
            elif op ==10:
                break

    ops = ( "1. Cadastrar jogo",
            "2. Editar jogo",
            "3. Excluir jogo",
            "4. Pesquisar jogo",
            "5. Listar jogo",
            "6. Registrar empréstimo",
            "7. Listar Empréstimos",
            "10. Sair")
    start(ops,jogo)
