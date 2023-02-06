a=int(input('Insira o valor de a: '))
if a == 0:
    print('A equação não pode ser do segundo grau! Experimente um valor maior ou igual a zero.')
elif a!=0:
    print('Proseguindo...')
b=int(input('Insira o valor de b: '))
c=int(input('Insira o valor de c: '))
delta=b*b-(4*a*c)
print(delta)
