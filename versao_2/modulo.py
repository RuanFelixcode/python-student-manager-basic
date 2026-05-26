def registrar_nome():
    while True:
        nome = input('digite seu nome:')
        if not nome.replace(' ','').isalpha():
            print('permitido apenas nomes simples ou compostos')
            continue
        return nome
        
def calcular_nota():
    while True:
        try:
            nota1 = float(input('digite sua primeira nota:'))
            nota2 = float(input('digite sua segunda nota:'))
            if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10:
                print('nota invalida!')
                continue
            media = (nota1 + nota2) / 2
            return media
                
        except ValueError:
             print('não aceitamos letras')


def verificar_aprovacao(media_aluno):
    if media_aluno >=7:
        return 'aprovado'
    elif media_aluno >=5:
        return 'recuperação'
    else:
        return 'reprovado'
    

def continuar():
    while True:
        opc = input('quer continuar s/n:').lower()
        if opc == 'n':
            return True
        elif opc == 's':
            return False
        else:
            print('opção invalida!') 
            continue
        
def cadastrar_alunos():
    alunos = {}
    while True:
        aluno = registrar_nome()
        aluno_media = calcular_nota()
        print(verificar_aprovacao(aluno_media))
        alunos.update({aluno:aluno_media})  
        if continuar():
            break
    return alunos
