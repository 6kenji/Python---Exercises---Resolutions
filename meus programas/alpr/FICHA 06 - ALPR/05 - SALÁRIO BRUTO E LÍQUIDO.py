salario = eval(input('Insira o seu salário: '))
desconto1 = salario * 0.10
desconto2 = (desconto1 * 0.05) + desconto1
print('O seu seu salário líquido é {}'.format(desconto2))
