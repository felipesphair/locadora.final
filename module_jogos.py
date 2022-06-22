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

























import csv
import os
import pandas as pd
from pip import main

jogo = {}

def jogos():

    def cadastrar_jogo(): 

        nome = input("Digite o nome: ")
        ano = input("Digite seu ano: ")
        categoria = input("Digite a categoria: ")

        jogo[nome] = [ano, categoria]

        colunas = ['ano', 'nome', 'categoria']
        file_exists = os.path.isfile('jogo.csv')
        with open('jogo.csv', 'a', newline='') as jogo_csv:
            cadastrar = csv.DictWriter(
                jogo_csv, fieldnames=colunas, delimiter=',', lineterminator='\r\n') 
            if not file_exists:
                cadastrar.writeheader()
            cadastrar.writerow(
                {'ano': ano, 'nome': nome.title(), 'categoria': categoria})

        print('Cadastro realizado com sucesso!')
        return


    def editar_jogo():  
        url = './jogo.csv'
        df = pd.read_csv(url)
        print(df) #IMPRIME A LISTA DE jogo NO TERMINAL, PRA PESSOA SABER O ID

        line_count = 0      
        idJogo = int(input("Digite o id do jogo que vc quer ditar: "))  #PERGUNTA O ID QUE A PESSOA QUER EDITAR
        idJogo += 2
        newName = (input("Digite o novo jogo: "))
        newYear= int(input("Digite o ano: "))  #ARMAZENA AS NOVAS INFORMACOES EM VARIAVEIS
        newCate = (input("Digite a categoria: "))


        with open("jogo.csv", 'r') as f: #ABRE O CSV
            reader = csv.reader(f, delimiter=',')

            lines = [] #VETOR LINES
            for line in reader:
                    line_count += 1
                    if idJogo == line_count: #CHECA SE O ID E IGUAL A LINHA DO CSV
                        line[0] = newYear #SETA AS NOVAS INFORMACOES NO VETOR LINE
                        line[1] = newName
                        line[2] = newCate
                    lines.append(line) #VETOR LINES PUXA O LINE

        with open("jogo.csv", 'w', newline='') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerows(lines)  #ESCREVE AS NOVAS INFORMACOES DO LINES NO CSV
        return #VOLTA PARA O MENU FILMES


    def excluir_jogo():
        url = './jogo.csv'
        df = pd.read_csv(url)
        print(df) #IMPRIME A LISTA DE jogo NO TERMINAL, PRA PESSOA SABER O ID

        line_count = 0      
        idJogo = int(input("Digite o id do jogo que vc deseja excluir: "))  #PERGUNTA O ID QUE A PESSOA QUER EXCLUIR
        idJogo += 2

        with open("jogo.csv", 'r') as f: #ABRE O CSV
            reader = csv.reader(f, delimiter=',')

            lines = [] #VETOR LINES
            for line in reader:
                    line_count += 1
                    if idJogo == line_count: #CHECA SE O ID E IGUAL A LINHA DO CSV
                        contador = line_count -1
                    lines.append(line) #VETOR LINES PUXA O LINE
                    
        del lines[contador]
        with open("jogo.csv", 'w', newline='') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerows(lines)  #ESCREVE AS NOVAS INFORMACOES DO LINES NO CSV
        return #VOLTA PARA O MENU
                


    def pesquisar_jogo():
        nome = input("Qual jogo deseja localizar? (Digite o nome): ")
        with open('jogo.csv') as jogo_csv:
            reader_obj = csv.reader(jogo_csv, delimiter=',')

            linhas = float
            linhas = 0
            for coluna in reader_obj:
                if linhas == 0:
                    linhas += 1
                else:
                    if coluna[1] == nome:
                        pesquisado = coluna[1]
                        print(f"Nome: {pesquisado} | Ano: {coluna[0]} | Categoria: {coluna[2]}")
                        return
                    else:
                        linhas += 1
            print("Jogo não localizado")
            return


    def lista_de_jogo():
        url = './jogo.csv'
        df = pd.read_csv(url)

        print(df)
        return


    def start(ops):
        while True:

            print("-" * 30)
            for op in ops:
                print(op)
            print("-" * 30)
            opt = int(input("Qual opção deseja escolher: "))

            if opt == 1:
                cadastrar_jogo()
            elif opt == 2:
                editar_jogo()
            elif opt == 3:
                excluir_jogo()
            elif opt == 4:
                alguem = pesquisar_jogo()
                if alguem != None:
                    print(alguem)
            elif opt == 5:
                lista_de_jogo()
            elif opt == 10:
                break
                
                
    ops = ( "1. Cadastrar jogo",
            "2. Editar jogo",
            "3. Excluir jogo",
            "4. Pesquisar jogo",
            "5. Listar jogo",
            #"6. Registrar empréstimo",
            #"7. Listar Empréstimos",
            "10. Sair")

    start(ops)
