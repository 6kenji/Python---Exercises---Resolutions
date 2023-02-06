print('Abaixo a lista de picolés à serem vendidos: ')
print('1.picolés do tipo 1 - 50 mts')
print('2.picolés do tipo 2 - 60 mts')
print('3.picolés do tipo 3 - 75 mts')
tipo = int(input('Escolha um tipo: '))
venda = int(input('Quantos deseja vender? '))
total1 = 50 * venda
total2 = 60 * venda
total3 = 75 * venda
if tipo == 1:
     print ('A quantidade vendida será de {}, e o total arrecadado é de: {} mts'.format(venda,total1))
elif tipo == 2:
     print ('A quantidade vendida será de {}, e o total arrecadado é de: {} mts'.format(venda,total2))
elif tipo == 3:
     print ('A quantidade vendida será de {}, e o total arrecadado é de: {} mts'.format(venda,total3))



