horas_de_trabalho = int(input('Quantas horas trabalhou ao mês? '))
ganho_por_hora = float(input('Qual é o seu lucro por hora? '))
salario = horas_de_trabalho * ganho_por_hora
salario2 = (horas_de_trabalho * ganho_por_hora) + (0.5 * ganho_por_hora)
if horas_de_trabalho >= 160:
    print('O seu salario é de: {} meticais'.format(salario2))
else:
    print('O seu salario é de: {} meticais'.format(salario))
