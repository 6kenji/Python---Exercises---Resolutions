#Nr 4 da ficha
def soma_dos_elementos4(x, n):
    s = 0
    for i in range(1, n+1):
        s = 1 + x + pow(x, n)/i
    print('A soma deste valor, em série é: {}'.format(s))
#Executar
x = int(input('Insira um valor inteiro para x: '))
n = int(input('Insira o outro valor pelo qual {} deve ser elevado: '.format(x)))
soma_dos_elementos4(x, n)