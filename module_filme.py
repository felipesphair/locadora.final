import csv
import os
import pandas as pd


def filme():
    def menu(ops):
        print("-" * 30)
        for op in ops:
            print(op)
        print("-" * 30)
        op = int(input("Qual opção deseja escolher: "))
        return op

    def cadastrar_filme():
        filme = {}

        nome = input("Digite seu nome: ")
        ano = input("Digite seu ano: ")
        categoria = input("Digite sua categoria: ")

        # buscar cliente cadastrado através de ano
        filme[ano] = [nome, categoria]

        colunas = ['ano', 'nome', 'categoria']  # colunas da tabela .csv
        file_exists = os.path.isfile('filme.csv')
        with open('filme.csv', 'a', newline='') as filme_csv:
            # DictWriter grava dados no formato de dicionário
            cadastrar = csv.DictWriter(
                filme_csv, fieldnames=colunas, delimiter=',', lineterminator='\r\n')  # fieldnames = nome de campos, ou seja -> colunas, divisor de dados sendo ',', lineterminator \r\n serve para quebrar a linha
            # caso não existe o arquivo 'file_exist', faz o fieldnames funcionar, visto que há o 'writeheader()'
            if not file_exists:
                # writeheader grava a primeira linha de arquivo csv usando os nomes de campo pré-especificados.
                cadastrar.writeheader()
            # escrever nas linhas em respectivas 'keys' e 'values', title() -> deixar letra maiuscula
            cadastrar.writerow(
                {'ano': ano, 'nome': nome.title(), 'categoria': categoria})

        print('Cadastro realizado com sucesso!')
        return filme

    def editar_filme(filme):
        alguem = pesquisar_filme(filme)
        if alguem == None:
            print("filme não localizada.")
            op = input("Gostaria de cadastrá-la? (s/n)")
            if op == "s":
                return cadastrar_filme()
            else:
                return None
        else:
            for i in range(len(filme) - 1):
                if filme[i] == alguem:
                    del(filme[i])
            cadastrar_filme()

    def excluir_filme(filme):
        alone = pesquisar_filme(filme)
        if alone == None:
            print("filme não localizadas.")
        else:
            # excluindo filme
            for i in range(len(filme) - 1):  # para i dentro da lista filmes
                if filme[i] == alone:
                    del(filme[i])

    def pesquisar_filme(filme):
        nome = input("Qual filme deseja localizar? (Digite o nome)")
        for filme in filme:
            if filme["nome"] == nome:
                return filme
        return None

    def listar_filme():
        url = './filme.csv'
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
                        codigo_filme = input("Digite seu codigo_filme: ")
                        data = input("Digite a data do filme: ")

                        colunas = ['codigo do filme', 'cpf', 'nome', 'data']  # colunas da tabela .csv
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
                                {'codigo do filme': codigo_filme, 'cpf': cpf, 'nome': pesquisado ,'data': data})

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



    def start(ops, filme):
        while True:
            op = menu(ops)
            if op == 1:
                filme = cadastrar_filme()
                filme.append(filme)
            elif op == 2:
                filme = editar_filme(filme)
            elif op == 3:
                alone = excluir_filme(filme)
            elif op == 4:
                alguem = pesquisar_filme(filme)
                if alguem != None:
                    print(alguem)
            elif op == 5:
                listar_filme()
            elif op == 6:
                realizar_emprestimo()
            elif op == 7:
                listar_emprestimos()
            elif op ==10:
                break

    ops = ( "1. Cadastrar filme",
            "2. Editar filme",
            "3. Excluir filme",
            "4. Pesquisar filme",
            "5. Listar filme",
            "6. Registrar empréstimo",
            "7. Listar Empréstimos",
            "10. Sair")
    start(ops,filme)
