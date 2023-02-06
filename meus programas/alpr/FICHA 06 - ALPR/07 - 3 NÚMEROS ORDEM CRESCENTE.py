x = eval(input('Insira o primeiro valor: '))
y = eval(input('Insira o segundo valor: '))
z = eval(input('Insira o terceiro valor: '))
#PRIMEIRAS CONDIÇÕES
if x > y > z:
    print(z,y,x)
elif x > z > y:
    print(y,z,x)
elif y > x > z:
    print(z,x,y)
elif y > z > x:
    print(x,z,y)
elif z > x > y:
    print(y,x,z)
elif z > y > x:
    print(x,y,z)
#OUTRAS CONDIÇÕES
if x > y  and x > z and z < y:
    print(z,y,x)
elif y > x and y > z and x > z:
    print(z, x, y)
elif z > x and z > y and y < x:
    print (y,x,z)
