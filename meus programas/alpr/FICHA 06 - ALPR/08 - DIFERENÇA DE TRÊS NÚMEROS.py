x = eval(input('Insira o primeiro valor: '))
y = eval(input('Insira o segundo valor: '))
z = eval(input('Insira o terceiro valor: '))
#OPERATION 1
diferenca1 = x - y
diferenca2 = x - z
#OPERATION 2
diferenca3 = y - x
diferenca4 = y - z
#OPERATION 3
diferenca5 = z - x
diferenca6 = z - y
#PROGRAMA PARA RODAR
if x > y and  z > y and x > z :
    print('A diferença é igual a {}'.format(diferenca1))
elif x > y and x > z and y > z:
    print('A diferença é igual a {}'.format(diferenca2))
#/////////////////////////////
if y > x and z > x and y > z :
    print('A diferença é igual a {}'.format(diferenca3))
elif y > x and y > z and z > x:
    print('A diferença é igual a {}'.format(diferenca4))
#/////////////////////////////
if z > x and y > x and z > y:
    print('A diferença é igual a {}'.format(diferenca1))
elif z > x and z > y and x > y:
    print('A diferença é igual a {}'.format(diferenca2))
#/////////////////////////////