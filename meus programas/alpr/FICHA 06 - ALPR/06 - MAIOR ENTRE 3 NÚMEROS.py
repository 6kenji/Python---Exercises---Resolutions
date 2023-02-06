print('Insira três numeros distintos')
x=float(input('Insira o primeiro valor: '))
y=float(input('Insira o segundo valor: '))
z=float(input('Insira o terceiro valor: '))
if x>y>z:
    print('O número {} é o maior'.format(x))
elif y>z>x:
    print('O número {} é o maior'.format(y))
elif z>y>x:
    print('O número {} é o maior'.format(z))
elif x>y==z:
    print('O número {} é o maior'.format(x))
elif y>x==z:
    print('O número {} é o maior'.format(y))
elif z>x==y:
    print('O número {} é o maior'.format(z))
elif x==y==z:
    print('Nenhum número é o maior, pois todos são iguais')
elif x<y==z:
    print('O número {} é o maior e está repetido'.format(y,z))
elif y<x==z:
    print('O número {} é o maior e está repetido'.format(x,z))
elif z<x==y:
    print('O número {} é o maior e está repetido'.format(x,y))

