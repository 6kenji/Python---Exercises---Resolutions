"""
Faça um programa que para o tuplo (12, 3, 2, 5, 7, 30, 2, 4, 2, 1,13) informa o
número de vezes que um certo número informado pelo utilizador ocorre no tuplo.
"""
def vezes(T):
    v = 0
    num = eval(input('Insira um número para saber quantas vezes o mesmo ocorre: '))
    for k in range(len(T)):
        if num == T[k]:
            v = v + 1
    print('O número informado é repetido, ',v,'vez(es)!')
T = (12, 3, 2, 5, 7, 30, 2, 4, 2, 1, 13)
vezes(T)