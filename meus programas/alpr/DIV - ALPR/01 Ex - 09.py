"""
Seja dado o tuplo (2, 4, 23, 1, 76, 3, 36), escreva um programa para imprimir o maior
elemento do tuplo.
"""
def maior_numero(Y):
    maior = 0
    for k in range(len(Y)):
        if Y[k] > maior:
            maior = Y[k]
    print(maior)
Y = (2, 4, 23, 1, 76, 3, 36)
maior_numero(Y)