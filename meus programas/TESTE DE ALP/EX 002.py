carros_vendidos = int(input('Insira o numero de carros vendidos: '))
valor_das_vendas = eval(input('Insira o total de vendas que foi arrecadado: '))
salario = 6850 + (1500 * carros_vendidos) + (valor_das_vendas * 0.05)
print('O seu salario e {}'.format(salario))
