import os

usuario = []
acervo = []


# LIMPAR TEXTO
def limpar():
    print("\n" * 20)


# classe de cores
class bcolors:
    OK = '\033[92m'  # GREEN
    WARNING = '\033[93m'  # YELLOW
    FAIL = '\033[91m'  # RED
    RESET = '\033[0m'  # RESET COLOR


def linha(tam=42):
    return '*' * tam


# funcao cabecalho centraliza o cabecalho e chama a funcao linha(hirarquia)
def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def cabecalhoMenu():
    print(linha())


# LIVRO
def listarTodos():
    for livros in acervo:
        cabecalho("Todos os livros em nosso acervo")
        print("Nome:", livros['nome'])
        print("codigo:", livros['codigo'])
        print("status:", livros['status'])
        cabecalhoMenu()
    op = input("Digite (1) para voltar ")
    if (op == "1"):
        menu()
    else:
        listarTodos()


def cadastrarlivro():
    codigo = input("codigo: ")
    nome = input("Nome: ")
    status = "Disponivel"

    livros = {'nome': nome, 'codigo': codigo, 'status': status}
    acervo.append(livros)


def consultarLivro(valor):
    for livros in acervo:
        if valor == livros['codigo']:
            cabecalho("Resultado da busca")
            print("Nome:", livros['nome'])
            print("codigo:", livros['codigo'])
            print("status:", livros['status'])
            cabecalhoMenu()
        else:
            print("Não temos esse livro em nosso acervo")


def editarLivro(valor):
    for livros in acervo:
        if valor == livros['codigo']:
            op = input("Digite (1) para reservar o livro: ")
            if (op == "1"):
                livros['status'] = "Reservado"
                print("Nome:", livros['nome'])
                print("codigo:", livros['codigo'])
                print("status:", livros['status'])
                cabecalhoMenu()
                print(bcolors.OK + "Alteração realizado com sucesso" + bcolors.RESET)
            else:
                print(bcolors.OK + "Operação cancelada" + bcolors.RESET)
        else:
            print(bcolors.WARNING + "Não temos esse livro em nosso acervo" + bcolors.RESET2)

    # LOGIN


def cadastrarUsuario():
    login = input("Digite o seu login: ")
    senha = input("Digite a sua senha: ")
    dadosUsuario = {'login': login, 'senha': senha}
    usuario.append(dadosUsuario)
    print(bcolors.OK + "Usuário cadastrado com sucesso! " + bcolors.RESET)


def validacaoLogin(usuarioLogin, usuarioSenha):
    for dadosUsuario in usuario:
        if usuarioLogin == dadosUsuario['login'] and usuarioSenha == dadosUsuario['senha']:
            limpar()
            print(bcolors.OK + "Bem vindo: ", usuarioLogin + bcolors.RESET)
            menu()
        else:
            print(bcolors.WARNING + "Usuário ainda não cadastrado" + bcolors.RESET)


def menu():
    op = 0
    while op != "8":
        op = input(bcolors.OK + ">>>Menu incial<<<" + bcolors.RESET + '''

1- Cadastrar um Livro
2- Consultar um Livro
3- Listar todos os Livros
4- alterar um livro
5- Login
6- Cadastrar
7- Logout

Escolha uma opção: ''')

        if (op == "1"):
            cadastrarlivro()
            # Enquanto a variavel receber 1 será feito um loop onde Será perguntado ao usuario se ele irá cadastrar outro livro
            opcaoCadastar = input("Desejar cadastrar outro livro (1) Sim (0) Voltar: ")
            while opcaoCadastar == "1":
                cadastrarlivro()
                opcaoCadastar = input("Desejar cadastrar outro livro (1) Sim (0) Voltar: ")

        elif (op == "2"):
            consultar = input('Digite o código do livro: ')
            if len(acervo) > 0:
                consultarLivro(consultar)
                # Enquanto a variavel receber 1 será feito um loop onde Será perguntado ao usuario se ele irá realozar a consulta novamente
                opcaoConsultaUnitario = input("Dessaja realizar outra busca (1) Sim (0) Não: ")
                while opcaoConsultaUnitario == "1":
                    if len(acervo) > 0:
                        consultar = input('Digite o código do livro: ')
                        consultarLivro(consultar)
                        opcaoConsultaUnitario = input("Dessaja realizar outra busca (1) Sim (0) Não: ")
                    else:
                        print(bcolors.FAIL + "Nosso acervo está vazio" + bcolors.RESET)
                        menu()
                else:
                    menu()

            else:
                print(bcolors.FAIL + "Nosso acervo está vazio" + bcolors.RESET)
                menu()



        elif (op == "3"):
            if len(acervo) > 0:
                listarTodos()
            else:
                print(bcolors.FAIL + "Nosso acervo está vazio" + bcolors.RESET)

        elif (op == "4"):
            if len(acervo) > 0:
                consultar = input('Digite o código do livro que deseja alterar: ')
                editarLivro(consultar)

            else:
                print(bcolors.FAIL + "Nosso acervo está vazio" + bcolors.RESET)


        elif (op == "5"):
            loginUsuario = input("Digite o seu login: ")
            validacaoLogin(loginUsuario)

        elif (op == "6"):
            cadastrarUsuario()
        elif (op == "7"):
            login()
        else:
            print("Opção invalida")


def login():
    # Tela login e cadastrado
    op = 0
    while op != "3":
        op = input(bcolors.OK + ">>>Tela lOGIN<<<" + bcolors.RESET + '''

        1- Login
        2- Cadastrar
        2- Sair do sistema


        Escolha uma opção: ''')

        # LOGIN
        if (op == "1"):
            loginUsuario = input("Digite o seu login: ")
            senhaUsuario = input("Digite a sua Senha: ")
            if len(usuario) > 0:
                validacaoLogin(loginUsuario, senhaUsuario)

            else:
                cabecalho(bcolors.WARNING + "Sistema ainda não possui nenhum Usuário cadastrado" + bcolors.RESET)
        # CADASTRAR
        elif (op == "2"):
            cadastrarUsuario()


login()



