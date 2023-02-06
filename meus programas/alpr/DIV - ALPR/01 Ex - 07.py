"""
Faça um programa que para um tuplo ele informa com true se o tuplo é constituído
exclusivamente de números pares e false caso o contrário (12, 3, 2, 5, 7, 30, 2, 4, 2,
1,13).
"""
def impar_par(K):
    contar = 0
    for k in range(len(K)):
        contar = contar + 1
        if K[k] % 2 == 0 and K[contar] % 2 == 0:
            return True
        else:
            return False

K = (12, 3, 2, 5, 7, 30, 2, 4, 2, 1, 13)
print('Verificação.....',impar_par(K))