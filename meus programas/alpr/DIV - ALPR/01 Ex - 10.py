"""
Seja dado o tuplo (12, 3, 2, 5, 7, 30, 2, 4, 2, 1,13), faça um programa que imprime a
quantidade de números pares e números ímpares contidos no vector
"""
def impar_par(K):
    contar_par = 0
    contar_impar = 0
    for k in range(len(K)):
        if K[k] % 2 == 0:
            contar_par = contar_par + 1
    print('O tuplo tem', contar_par, 'números pares.')
    for k in range(len(K)):
        if K[k] % 2 != 0:
            contar_impar = contar_impar + 1
    print('O tuplo tem', contar_impar, 'números ímpares.')
K = (12, 3, 2, 5, 7, 30, 2, 4, 2, 1,13)
impar_par(K)