def tipo_de_número(n):
    if n == 0 or n < 0:
        print('O número {} é do tipo: "N"'.format(n))
    elif n > 0:
        print('O número {} é do tipo: "P"'.format(n))
#Executar
n = eval(input('Insira um número qualquer: '))
tipo_de_número(n)
