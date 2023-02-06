"""
Faça um programa recursivo que determina o produto de dois números
x*y=?
4*3=3+3+3+3=4+4+4=12
"""
def produto(x,y):
    if y == 0 or x == 0:
        return 0
    else:
        return x + produto(x,y-1)
x = int(input('Insira um número: '))
y = int(input('Insira um outro número: '))
print('O resultado:',produto(x, y))