"""
Faça um programa que calcula o produto dos elementos de um tuplo
(1,2,3,4,5,6,7,8,9)
"""
def produto(K):
    p = (K[0]*K[1]*K[2]*K[3]*K[4]*K[5]*K[6]*K[7]*K[8])
    print('O produto dos elementos do tuplo K é: ', p)
K = (1,2,3,4,5,6,7,8,9)
produto(K)