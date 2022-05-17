import os
#usuario padrão de incio adm
#lista
tUsuarios = list()
tlivros= list()
#dicioanrio
usuarios = {'login':'adm','senha':'adm'}


livros = dict()
biblioteca = list()

#linha esta definido para o tamanho com 42 caracteres
def linha(tam=42):
    return '*' * tam

#funcao cabecalho centraliza o cabecalho e chama a funcao linha(hirarquia)
def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menuI(listaInical):
    cabecalho('Tela inicial')
    cont = 1
    for item in listaInical:
        print(f'{cont}-{item}')
        cont += 1

def livrosDisponiveis(tlivros):
    cabecalho('livros disponiveis')
    print('Descricao ')
    cont = 1
    for item in tlivros:
        print(f'{cont}-{item}')
        cont += 1
#funcao menu lista os menus inicais - cadastrar e login

def menu(lista):
    cabecalho('Reserva de livros')
    cont = 1
    for item in lista:
        print(f'{cont}-{item}')
        cont +=1



#loop enquanto a varivel opcao_incial não  receber 1 ou 2 será redireicionado para a tela de login
    while True:
        opcao_tela_incial = input("Sua opção: ")
        if opcao_tela_incial in '12':
            break
        print('\033[33m' + 'Favor digite 1 para realizar o login ou 2 para se cadastrar' + '\033[0;0m')

    if opcao_tela_incial == "1":
        (cabecalho('Tela Login'))
        login = input("Digite seu login: ")
        senha = input("Digite sua senha: ")
        if(login==usuarios['login']) and (senha == usuarios['senha']):
            print('\033[32m'+'Seka bem vindo Sr',login+'\033[0;0m')
            menuI(['Pesquisar', 'Cadastrar Livro','Sair do sistema'])
            while True:
                opcao_menu_incial = input("Sua opção: ")
                if opcao_menu_incial in '123':
                    break
                print('\033[33m' + 'Favor digite 1 para realizar a pesquisa, 2 para cadastrar um livro ou 3 para Sair do sistema' + '\033[0;0m')
            if(opcao_menu_incial=="1"):
                print("deu certp")
                for e in biblioteca:
                    for v in e.values():
                        print(v, end=' ')
                    print()

            elif(opcao_menu_incial=="2"):
                for c in range(0, 2):
                    livros['codigo'] = str(input('Digite o codigo do livro :'))
                    livros['descricao'] = str(input('Digite a descricao do livro :'))
                    livros['status'] = str(input('Digite o status do livro :'))
                    biblioteca.append(livros.copy())
                menuI(['Pesquisar', 'Cadastrar Livro', 'Sair do sistema'])
                while True:
                    opcao_menu_incial = input("Sua opção: ")
                    if opcao_menu_incial in '123':
                        break
                    print('\033[33m' + 'Favor digite 1 para realizar a pesquisa, 2 para cadastrar um livro ou 3 para Sair do sistema' + '\033[0;0')

        else:
            print('\033[31m'+'Dados incorretos'+'\033[0;0m')
            menu(lista)

    #tela de cadastro se a variavel opcao inical receber 2 será direceionado para tela de cadastro
    elif(opcao_tela_incial=="2"):
        (cabecalho('Tela Cadastro Usuario'))
        new_user = input("Digite o seu login: ")
        new_password = input("Digite a sua senha: ")
        usuarios['login'] = new_user
        usuarios['senha'] = new_password
        # a lista vai listando os usuarios cadastrados no dicionario
        tUsuarios.append(usuarios.copy())
        print(tUsuarios)

        print('\033[32m'+'Usuario cadastrado'+'\033[0;0m')
        menu(lista)
    # tela inical se a variavel opcao inical receber um valor diferente de 1 ou 2 será redireceionado para tela de login


menu(['Login','cadastra-se'])


