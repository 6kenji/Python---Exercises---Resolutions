def soma_em_série(x, k):
    s = 0
    for k in range (k + 1):
        s = s + pow(x, k)
    print('A operação é igual a {}'.format(s))
####EXECUTAR
x = int(input('Insira um valor inteiro para x: '))
k = int(input('Agora insira um valor pelo qual se deve elevar o x, (k): '))
soma_em_série(x, k)
