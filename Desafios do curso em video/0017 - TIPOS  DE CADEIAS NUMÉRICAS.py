n = int(input('Insira um número no intervalo de 0 a 9999: '))
print('A unidade é : {}'.format( n // 1 % 10 ))
print('A dezena é : {}'.format( n // 10 % 10 ))
print('A centena é : {}'.format( n // 100 % 10 ))
print('O milhar é : {}'.format( n // 1000 % 10 ))