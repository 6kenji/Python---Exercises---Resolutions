x = eval(input('Insira o primeiro valor: '))
y = eval(input('Insira o segundo valor: '))
z = eval(input('Insira o terceiro valor: '))
if x > y > z:
    print(z,y,x)
elif y > x > z:
    print(z,x,y)
elif z > x > y:
    print(y,x,z)
elif x > y < z:
    print(z,x,y)
elif z > y < x:
    print(x,z,y)
elif y > z < x:
    print(x,y,z)
elif x < y > z:
    print(y,z,x)
elif y < x > z:
    print(z,y,x)
elif x < z > y:
    print(z,x,y)
