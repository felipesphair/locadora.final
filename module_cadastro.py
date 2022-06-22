import csv
import os
import pandas as pd

pessoa = {}

def cliente():
    def menu(ops):
        print("-" * 30)
        for op in ops:
            print(op)
        print("-" * 30)
        op = int(input("Qual opção deseja escolher: "))
        return op
        

    def cadastrar_pessoa(): 


        with open('clientes.csv', 'r') as arquivo:
            arquivo_csv = csv.reader(arquivo, delimiter=',')
            lst = list(arquivo_csv) 
            for linha in arquivo_csv:
                print(linha)

        nome = input("Digite seu nome: ")
        cpf = input("Digite seu cpf: ")
        idade = input("Digite sua idade: ")

        pessoa[cpf] = [nome, idade] #buscar cliente cadastrado através de cpf

        colunas = ['cpf', 'nome', 'idade'] #colunas da tabela .csv
        file_exists = os.path.isfile('clientes.csv')
        with open('clientes.csv', 'a', newline='') as clientes_csv:
            #DictWriter grava dados no formato de dicionário
            cadastrar = csv.DictWriter(
                clientes_csv, fieldnames=colunas, delimiter=',', lineterminator='\r\n') #fieldnames = nome de campos, ou seja -> colunas, divisor de dados sendo ';', lineterminator \r\n serve para quebrar a linha
            #caso não existe o arquivo 'file_exist', faz o fieldnames funcionar, visto que há o 'writeheader()'
            if not file_exists:
                #writeheader grava a primeira linha de arquivo csv usando os nomes de campo pré-especificados.
                cadastrar.writeheader()
            # escrever nas linhas em respectivas 'keys' e 'values', title() -> deixar letra maiuscula
            cadastrar.writerow(
                {'cpf': cpf, 'nome': nome.title(), 'idade': idade})

        print('Cadastro realizado com sucesso!')
        return pessoa
        cliente()

    def editar_pessoa():
        print('comeco')
        alguem = pesquisar_pessoa()
        if alguem == None:
            op = input("Gostaria de cadastrá-la? (s/n)")
            if op == "s":
                return cadastrar_pessoa()
            else:
                print('meio')
                return None
        else:
            print('fim')
            for i in range(5):
                print('AAAAA')
                print(i)
                print('aaaaaaa')
                if i == alguem:
                    del(i)
            
            cadastrar_pessoa()
            cliente()


    def excluir_pessoa():
        return_nome = pesquisar_pessoa()
        if return_nome != None:
            url = 'clientes.csv'
            df = pd.read_csv('clientes.csv')
            print(df) 
            df.pop(1) 
            print(df)

            cliente()

              

    def lista_de_clientes():
        url = './clientes.csv'
        df = pd.read_csv(url)

        print(df)
        cliente()
                


    def pesquisar_pessoa():
        cpf = input("Qual pessoa deseja localizar? (Digite o cpf)")
        with open('clientes.csv') as clientes_csv:
            reader_obj = csv.reader(clientes_csv, delimiter=',')

            linhas = float
            linhas = 0
            for coluna in reader_obj:
                if linhas == 0:
                    linhas += 1
                else:
                    if coluna[0] == cpf:
                        pesquisado = coluna[1]
                        print(f"Nome: {pesquisado} | idade: {coluna[2]}")
                        return pesquisado
                    else:
                        linhas += 1
            print("pessoa não localizada")
            return None
            cliente()

    def lista_de_clientes():
        url = './clientes.csv'
        df = pd.read_csv(url)

        print(df)
        cliente()

    def start(ops):
        while True:
            op = menu(ops)
            if op == 1:
                cadastrar_pessoa()
            elif op == 2:
                editar_pessoa()
            elif op == 3:
                excluir_pessoa()
            elif op == 4:
                alguem = pesquisar_pessoa()
                if alguem != None:
                    print(alguem)
            elif op == 5:
                lista_de_clientes()
            elif op == 6:
                break

    ops = ("1. Cadastrar pessoa",
           "2. Editar pessoa",
           "3. Excluir pessoa",
           "4. Pesquisar pessoa",
           "5. Lista de clientes",
           "6. Sair")
    


    start(ops)
