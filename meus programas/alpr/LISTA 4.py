#Informar quantas vezes o "x" e repetido na funcao K = [12,3,2,4,5,6,8,3,4,1,0]
def vezes_repetidas(x):
    cont = 0
    while cont != x:
        print('O numero {} nao e repetido'.format(x))
        for i in range(len(K)):
            x = K[i]
            if cont == x:
                print('O numero {} foi repetido'.format(x))
#Executar
x = eval(input('Insira um valor: '))
K = [12,3,2,4,5,6,8,3,4,1,0]
vezes_repetidas(x)