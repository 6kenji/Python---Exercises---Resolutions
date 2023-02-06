"""Formas de multiplicar vários números"""
#1
k = eval(input('Insira um número qualquer: '))
print('A tabuada de {} é:'.format(k))
print('-'* 10)
print('{} × {} = {}'.format(1,k,1*k))
print('{} × {} = {}'.format(2,k,2*k))
print('{} × {} = {}'.format(3,k,3*k))
print('{} × {} = {}'.format(4,k,4*k))
print('{} × {} = {}'.format(5,k,5*k))
print('{} × {} = {}'.format(6,k,6*k))
print('{} × {} = {}'.format(7,k,7*k))
print('{} × {} = {}'.format(8,k,8*k))
print('{} × {} = {}'.format(9,k,9*k))
print('{} × {} = {}'.format(10,k,10*k))
print('{} × {} = {}'.format(11,k,11*k))
print('{} × {} = {}'.format(12,k,12*k))
print('-'* 15)
#2
k = eval(input('Insira um número qualquer: '))
for i in range(1,13):
    print('{} × {} = {}'.format(i, k, i * k))