"""
Faça um programa que determina a média dos elementos que estão dentro de um
tuplo T (19, 16, 13, 8, 18).
"""
def média(T):
    m = (T[0]+T[1]+T[2]+T[3]+T[4])/len(T)
    print('A média dos elementos do tuplo T é: ', m)
T = (19, 16, 13, 8, 18)
média(T)
