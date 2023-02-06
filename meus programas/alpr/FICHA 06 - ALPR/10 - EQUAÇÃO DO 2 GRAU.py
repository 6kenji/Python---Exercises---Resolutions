a=eval(input('Insira o valor de a: '))
if a == 0:
    print('A equação não pode ser do segundo grau! Experimente um valor maior ou igual a zero.')
elif a!=0:
    print('Proseguindo...')
b=eval(input('Insira o valor de b: '))
c=eval(input('Insira o valor de c: '))
delta=b**2-(4*a*c)
print('Delta igual a {}'.format(delta))
x1=( - b + (delta**0.5))/(2*a)
x2=( - b - (delta**0.5))/(2*a)
print('x1=',x1,'x2=',x2)
