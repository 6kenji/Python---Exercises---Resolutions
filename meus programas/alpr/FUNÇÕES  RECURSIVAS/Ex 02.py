"""
Faça um programa recursivo que determina a potencia de um número
x^y=?
3^2=9
3^0=1
0^1000=0
"""
def exp(x,y):
    if x == 0 and y == 0:
        print(False)
    elif x == 0:
        return 0
    elif y == 0:
        return 1
    else:
        return x * exp(x,y-1)
x = int(input('Insira um número: '))
y = int(input('Insira um outro número: '))
print('Resultado:',exp(x, y))