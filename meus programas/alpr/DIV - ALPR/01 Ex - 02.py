"""
Faça um programa para verificar se um número existe em um vector e quantas
vezes aparece no vector (12, 3, 2, 5, 7, 30, 2, 4, 2, 1,13)
"""
def verificação(n):
    contar = 0
    if n in K:
        for i in K:
            if i in K and i == n:
                contar = contar + 1
        print('O número existe  no tuplo. ')
        print('Aparece também', contar, 'vez(es)')
    if not n in K:
        print('O número não existe  no tuplo. ')
K = (12, 3, 2, 5, 7, 30, 2, 4, 2, 1,13)
n = eval(input('Insira um número para verificação: '))
verificação(n)
