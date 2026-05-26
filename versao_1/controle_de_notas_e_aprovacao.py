# declaraçao de variaveis simples e compostas
alunos = []
notas = []
soma = 0
aprovados = 0
reprovados = 0
turma = {}
# aqui ocorre a validaçao da senha
tentativas = 0
senha = int(input('digite a senha para entrar no sistema:'))
if senha != 123:
    print('senha incorreta voce tem mais 3 tentativas para digitar a senha correta')
while senha != 123:
    senha = int(input('digite a senha correta para entrar no sistema:'))
    tentativas += 1 
    if tentativas == 1 :
        print('voce tem mais 2 tentativas')
    elif tentativas == 2 :
        print('voce tem mais 1 tentativas')
    elif tentativas == 3 :
        print('limite execido')
        break
if senha == 123:
    print('bem vindo ao sistema')
        
else:
    print('descupe infelismente voce nao podera entrar no sistema')
while senha == 123:
    print('''menu de opçoes
    nome aluno [1]
    inserir notas da turma [2]
    sair [3]''')
    opc = int(input('selecione uma opçao:'))
    if opc == 1 :
        aluno = input('digite o nome do aluno:')
        alunos.append(aluno)
    elif opc == 2:
        nota = float(input('digite a nota:'))
        if nota > 7 :
            aprovados += 1 
        else:
            reprovados += 1
        notas.append(nota)
        soma = nota + soma
    elif opc == 3 :
        break
    turma = dict(zip(alunos,notas))
    
print(f'lista de alunos {turma}')
print(f'quantidade de aprovados {aprovados}')
print(f'quantidade de reprovados {reprovados}')
print(f'media da turma {soma/len(notas)}')
