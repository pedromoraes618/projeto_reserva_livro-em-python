def cadastro():
    nome = input('Nome:').lower()
    curso = input('Curso:').lower()
    idade = int(input('Idade:'))
    dados_aluno = {'nome': nome, 'curso': curso, 'idade': idade}
    aluno.append(dados_aluno)


aluno = [{'nome': 'marcelo', 'curso': 's.i', 'idade': 38}, {'nome': 'mariana', 'curso': 's.i', 'idade': 22}, {
    'nome': 'clara', 'curso': 's.i', 'idade': 20}, {'nome': 'junior', 'curso': 's.i', 'idade': 23}]

print('Alunos já cadastrados \n', aluno)
print('='*20)
cad = input('Deseja cadastrar um novo aluno: s/n').lower()
if cad == 's':
    cadastro()
print('='*40)
print(aluno)
print('-'*40)
# consultar cadastro
print('Consulta de de aluno por nome.')
consulta = input('Digite o nome do aluno:')
for linha in aluno:
    if linha['nome'] == consulta:
        print('Nome:', linha['nome'], 'Curso:', linha['curso'])
# >>>posição  - e deletar cadastro

posicao = -1
pesq = input('Digite o nome do aluno:')
for linha in aluno:
    posicao = posicao+1
    if linha['nome'] == pesq:
        print(aluno[posicao])
        print('='*30)
        print(posicao, 'é do tipo:', type(posicao))
        print('Agora vou alterar somente o nome esse cadastro')
        print('-'*50)
        novo = input('nome').lower()
        linha['nome'] = str(novo)
        print('- + -'*30)
        print(' # '*50)
        print(aluno[posicao])
    else:
        print('não localizado!')
print('#'*50)
print(aluno)