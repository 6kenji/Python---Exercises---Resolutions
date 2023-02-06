def soma_argumentos(x,y,z):
    s = x + y + z
    print('A soma destes três argumentos é igual a: {}'.format(s))
    return s
#Executar
x = eval(input('Insira o valor do primeiro argumento: '))
y = eval(input('Insira o segundo argumento: '))
z = eval(input('Agora o terceiro: '))
soma_argumentos(x,y,z)