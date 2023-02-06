def soma_em_série3(k):
    s = 0
    i = 1
    controlador = 0
    while controlador != k:
        s = s + 1/i
        i = i + 2
        controlador = controlador + 1
    print('A soma é igual a',s)
k = int(input('Insira um valor inteiro qualquer: '))
soma_em_série3(k)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
#Nr 3 da ficha