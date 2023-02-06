def soma_em_série2(n):
    s = 0
    for k in range (1,n+1):
        s = s + 1/k
    print('A soma é igual a {}'.format(s))
####Executar
n = int(input('Insira um valor inteiro qualquer: '))
soma_em_série2(n)
#Nr 2 da ficha