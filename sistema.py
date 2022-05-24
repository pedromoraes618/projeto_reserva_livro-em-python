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
        cabecalho("Todos os livros em nosso acervo || All books in our collection")
        print("Nome:", livros['nome'])
        print("codigo:", livros['codigo'])
        print("status:", livros['status'])
        cabecalhoMenu()
    op = input("Digite (1) para voltar || Type (1) to go back: ")
    if (op == "1"):
        menu()
    else:
        listarTodos()


def cadastrarlivro():
    codigo = input("Código: ")
    nome = input("Nome: ")
    status = "Disponivel"

    livros = {'nome': nome, 'codigo': codigo, 'status': status}
    acervo.append(livros)


def consultarLivro(valor):
    for livros in acervo:
        if valor == livros['codigo']:
            cabecalho("Resultado da busca || Search result")
            print("Nome:", livros['nome'])
            print("codigo:", livros['codigo'])
            print("status:", livros['status'])
            cabecalhoMenu()



def reservarLivro(valor):
    for livros in acervo:
        if valor == livros['codigo']:
            # if(livros['status']=="Reservado"):
            #     print(bcolors.WARNING +"O livro já está reservado"+ bcolors.RESET)
            #     menu()
            # else:
                op = input(bcolors.WARNING + "Digite (1) para reservar o livro || Enter (1) to reserve the book: " + bcolors.RESET)
                if (op == "1"):
                    livros['status'] = "Reservado"
                    print("Nome:", livros['nome'])
                    print("codigo:", livros['codigo'])
                    print("status:", livros['status'])
                    cabecalhoMenu()
                    print(bcolors.OK + "Livro reservado com sucesso || Book successfully booked" + bcolors.RESET)
                else:
                    print(bcolors.WARNING + "Operação cancelada || Operation canceled" + bcolors.RESET)
        # else:
        #     print(bcolors.WARNING + "Não temos esse livro em nosso acervo" + bcolors.RESET)
        #     menu()

def excluirLivro(valor):
    cont = -1
    for livros in acervo:
        cont = cont+1
        if livros['codigo'] == valor:
            del acervo[cont]
            print(bcolors.OK + "Livro deletado com sucesso || Successfully deleted book" + bcolors.RESET)




def cadastrarUsuario():
    login = input("Digite o seu login || Enter your login: ")
    senha = input("Digite a sua senha || Enter your password: ")
    dadosUsuario = {'login': login, 'senha': senha}
    usuario.append(dadosUsuario)
    print(bcolors.OK + "Usuário cadastrado com sucesso || User registered successfully! " + bcolors.RESET)


def validacaoLogin(usuarioLogin, usuarioSenha):
    for dadosUsuario in usuario:
        if usuarioLogin == dadosUsuario['login'] and usuarioSenha == dadosUsuario['senha']:
            limpar()
            print(bcolors.OK + "Bem vindo || Welcome: ", usuarioLogin + bcolors.RESET)
            menu()
        else:
            print(bcolors.WARNING + "Usuário ainda não cadastrado" + bcolors.RESET)


def menu():
    op = 0
    while op != "8":
        op = input(bcolors.OK + ">>>Menu incial || Start Menu <<<" + bcolors.RESET + '''

1- Cadastrar um Livro || Register a Book
2- Consultar um Livro || Consult a Book
3- Listar todos os Livros || List all books
4- Reservar um Livro || Resever a book
5- Excluir Livro || Delete Book
6- Cadastrar Usuário || Register user
7- Logout

Escolha uma opção || Choose an option: ''')

        if (op == "1"):
            cadastrarlivro()
            # Enquanto a variavel receber 1 será feito um loop onde Será perguntado ao usuario se ele irá cadastrar outro livro
            opcaoCadastar = input("Desejar cadastrar outro livro (1) Sim (0) Voltar || Want to register another book (1) Yes (0) Back:  ")
            while opcaoCadastar == "1":
                cadastrarlivro()
                opcaoCadastar = input("Desejar cadastrar outro livro (1) Sim (0) Voltar || Want to register another book (1) Yes (0) Back: ")

        elif (op == "2"):
            consultar = input('Digite o código do livro || Enter the book code:: ')
            if len(acervo) > 0:
                consultarLivro(consultar)
                # Enquanto a variavel receber 1 será feito um loop onde Será perguntado ao usuario se ele irá realozar a consulta novamente
                opcaoConsultaUnitario = input("Dessaja realizar outra busca (1) Sim (0) Não || "
                                              "Would you like to perform another search (1) Yes (0) No:  ")
                while opcaoConsultaUnitario == "1":
                    if len(acervo) > 0:
                        consultar = input('Digite o código do livro || Enter the book code: ')
                        consultarLivro(consultar)
                        opcaoConsultaUnitario = input("Dessaja realizar outra busca (1) Sim (0) Não ||"
                                                      " Would you like to perform another search (1) Yes (0) No: ")
                    else:
                        print(bcolors.FAIL + "Nosso acervo está vazio || Our collection is empty" + bcolors.RESET)
                        menu()
                else:
                    menu()

            else:
                print(bcolors.FAIL + "Nosso acervo está vazio || Our collection is empty" + bcolors.RESET)
                menu()



        elif (op == "3"):
            if len(acervo) > 0:
                listarTodos()
            else:
                print(bcolors.FAIL + "Nosso acervo está vazio || Our collection is empty" + bcolors.RESET)

        elif (op == "4"):
            if len(acervo) > 0:
                consultar = input('Digite o código do livro que deseja reservar || Enter the code of the book you want to book:: ')
                consultarLivro(consultar)
                reservarLivro(consultar)

            else:
                print(bcolors.FAIL + "Nosso acervo está vazio || Our collection is empty" + bcolors.RESET)


        elif (op == "5"):
            excluir = input("Digite o código do livro a ser excluido || Enter the book code to be unique: ")

            excluirLivro(excluir)

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
        op = input(bcolors.OK + ">>>Tela lOGIN || Login Screen<<<" + bcolors.RESET + '''

        1- Login
        2- Cadastrar || register
        3- Sair do sistema || Exit system


        Escolha uma opção || Choose an option:: ''')

        # LOGIN
        if (op == "1"):
            loginUsuario = input("Digite o seu login || Enter your login: ")
            senhaUsuario = input("Digite a sua Senha || Enter your Password: ")
            if len(usuario) > 0:
                validacaoLogin(loginUsuario, senhaUsuario)

            else:
                cabecalho(bcolors.WARNING + "Sistema ainda não possui nenhum Usuário cadastrado || "
                                            "System does not have any registered User yet." + bcolors.RESET)
        # CADASTRAR
        elif (op == "2"):
            cadastrarUsuario()
    else:
         print("Sair do sistema || Exit system")


login()



