from random import randint
def sorteio():
    sorteiador = randint(0,1000)
    print(sorteiador)
    palpite = eval(input('Insira um palpite: '))
    tentativa = 1
    if palpite == sorteiador:
        print('Acertou')
    elif palpite > sorteiador:
        print('Insira um numero menor')
    else:
        print('Insira um numero maior')
    while palpite != sorteiador:
        palpite = eval(input('Insira de novo um palpite: '))
        tentativa = tentativa + 1
    print('Foram realizadas', tentativa,'tentativas!')
#Execução
sorteio()