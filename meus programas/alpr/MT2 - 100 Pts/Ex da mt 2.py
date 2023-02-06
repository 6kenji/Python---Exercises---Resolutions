def soma_em_serie(k):
    s = 0
    i = 1
    cont = 0
    while cont != k:
        cont = cont + 2
        i = i + 2
        s = 1 + pow(k, 1) / i
    print('A soma deste valor, em série é: {}'.format(s))
# Executar
k = int(input('Insira um valor inteiro para k: '))
soma_em_serie(k)
