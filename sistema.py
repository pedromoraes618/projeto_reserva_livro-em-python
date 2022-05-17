import os
usuarios = {'login':'adm','senha':'adm'}

#linha esta definido para o tamanho com 42 caracteres
def linha(tam=42):
    return '-' * tam
#funcao cabecalho centraliza o cabecalho e chama a funcao linha(hirarquia)
def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

#funcao menu chama a funcao cabecalho inserindo a string()g
def menu(lista):
    cabecalho('Tela inicial')
    cont = 1
    for item in lista:
        print(f'{cont}-{item}')
        cont +=1

#tela login, se selecionado a opção 1 será direicionado para a tela de login
    opcao_inicial = input("Sua opção: ")

    if opcao_inicial == "1":
        (cabecalho('Tela Login'))
        login = input("Digite seu login: ")
        senha = input("Digite sua senha: ")
        if(login==usuarios['login']) and (senha == usuarios['senha']):
            print("Seja bem vindo Sr",login)
        else:
            print("Dados incorretos")
            menu(lista)


    #tela de cadastro se a variavel opcao inical se selecionado a opcao 2 será direceionado para tela de cadastro
    elif(opcao_inicial=="2"):
        (cabecalho('Tela Cadastro'))
        new_user = input("Digite o seu login: ")
        new_password = input("Digite a sua senha: ")
        usuarios['login'] = new_user
        usuarios['senha'] = new_password
        print("Usuario cadastrado!")
        menu(lista)
    elif(opcao_inicial!="1" or "2"):
        print("Favor digite 1 para realizar o login ou 2 para se cadastrar")
        menu(lista)

menu(['Login','cadastra-se'])
