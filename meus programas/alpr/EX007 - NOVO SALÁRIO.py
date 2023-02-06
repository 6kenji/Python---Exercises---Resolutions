print('Seja bem vindo ao site oficial de reajuste salarial!')
nome = str(input('Insira o seu nome: '))
print('{}, abaixo temos a lista de cada categoria e o seu respectivo aumento salarial'.format(nome))
print('1.A, C, F, e H  10% de aumento sobre o salário;')
print('2.B, D, E, I, J e T 15% de aumento sobre o salário;')
print('3.K e R 25% de aumento sobre o salário;')
print('4.L, M, N, O, P, Q e S 35% de aumento sobre o salário; ')
print('5.U, V, X, Y, W e Z 50% de aumento sobre o salário.')
salario_actual=int(input('Insira o valor do seu salário actual: '))
categoria=float(input("Insira a sua categoria, para o beneficio de seu aumento: "))
ns = (salario_actual/0.1)
ns2 = (salario_actual/0.15)
ns3 = (salario_actual/0.25)
ns4 = (salario_actual/0.35)
ns5 = (salario_actual/0.50)
# noinspection PyTypeChecker
if categoria > 5:
    print('Opção inválida!')
if categoria == 1:
    print('{}, o seu novo salário é: {:.2f} mts'.format(nome, ns))
elif categoria == 2:
    print('{}, o seu novo salário é: {:.2f} mts'.format(nome, ns2))
elif categoria == 3:
    print('{}, o seu novo salário é: {:.2f} mts'.format(nome, ns3))
elif categoria == 4:
    print('{}, o seu novo salário é: {:.2f} mts'.format(nome, ns4))
elif categoria == 5:
    print('{}, o seu novo salário é: {:.2f} mts'.format(nome, ns5))
print('Obrigado por usar nossos serviços!!')






