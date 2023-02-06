"""
Faça um programa que recebe um tuplo de números e retorna o número de
elementos pares no tuplo (10, 2 , 13 , 23, 12, 15, 20, 50, 61, 73)
"""
def pares(K):
    for i in range(len(K)):
        if K[i] % 2 == 0:
            print(K[i])
K = (10, 2, 13, 23, 12, 15, 20, 50, 61, 73)
pares(K)
