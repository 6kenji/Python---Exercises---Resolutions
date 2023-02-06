def n_linha(n):
    contar = 1
    space = ' '
    if n == 0:
        print(0)
    if n >= 1:
        contar = contar + 1
        print(contar, end ='')
        for k in range(1,contar):
            print(k, end ='')
n = int(input('Insira um numero: '))
n_linha(n)
"""contar = 1
n_espaços = ''
while contar >= 1:
    print(n_espaços, end='')
    for n in range(1,contar):
        print(n, end='')"""
