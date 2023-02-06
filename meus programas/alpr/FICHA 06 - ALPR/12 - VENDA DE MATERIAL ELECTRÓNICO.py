nome=str(input('Insira o seu nome: '))
print('1.Vendas maiores que 50.000 mts - comissão de 12%')
print('2.Vendas nos extremos de 30.000 e 50.000 mts - comissão de 9.5%')
print('3.Vendas  em qualquer valor - comissão de 7%')
valor=float(input('{}, insira o valor de suas vendas, em meticais: '.format(nome)))
comissao1 = (valor * 0.12) + valor
comissao2 = (valor * 0.95) + valor
comissao3 = (valor * 0.70) + valor
if valor > 50000:
  print('{},a sua comissão é de: {} meticais'.format(nome, comissao1))
elif valor > 30000 or valor < 50000:
    print('{}, a sua comissão é de: {} meticais'.format(nome,comissao2))
elif valor < 30000 :
    print('{}, a sua comissão é de: {} meticais'.format(nome,comissao3))
print('Obrigado!')
