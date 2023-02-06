numero = eval(input('Insira um numero: '))
k = 0
contar = 0
#Instrucao
while k <= numero or contar < 2:
    k = k + 1
    numero1 = numero % k
    if numero1 == 0:
       contar = contar + 1
    if contar == 2:
        print('O numero {} e primo'.format(numero))
    elif contar < 2:
        print('{} nao e primo'.format(numero))
