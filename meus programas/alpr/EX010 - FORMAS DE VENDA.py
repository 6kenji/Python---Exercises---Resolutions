print('Bem vindo ao ambiente online da nossa loja!')
preco=float(input('Insira o valor das vendas em meticais: '))
print('Eis abaixo a lista de vendas juntamente de seus respectivos descontos.')
print('1.Venda a Vista - desconto de 10% ')
print('2.Venda a Prazo 30 dias - desconto de 5% ')
print('3.Venda a Prazo 60 dias - mesmo preço ')
print('4.Venda a Prazo 90 dias - acréscimo de 5% ')
print('5.Venda com cartão de débito - desconto de 8% ')
print('6.Venda com cartão de crédito - desconto de 7')
opcao=int(input('Escolha a opção: '))
d1=preco*0.1
d2=preco*0.05
d3=preco
d4=preco/0.05
d5=preco*0.08
d6=preco*0.07
if opcao == 1:
    print('Venda a Vista, pagamento a ser feito é de: {} mts'.format(d1))
elif opcao == 2:
    print('Venda a Prazo de 30 dias, pagamento a ser feito é de: {} mts'.format(d2))
elif opcao == 3:
    print('Venda a Prazo de 60 dias, pagamento a ser feito é de: {} mts'.format(d3))
elif opcao == 4:
    print('Venda a Prazo de 90 dias, pagamento a ser feito é de: {} mts'.format(d4))
elif opcao == 5:
    print('Venda com cartão de débito, pagamento a ser feito é de: {} mts'.format(d5))
elif opcao == 6:
    print('Venda com cartão de crédito, pagamento a ser feito é de: {} mts'.format(d6))
# opcao2=str(input('Prosseguir? 1.Sim ou 2.Não '))
# if opcao2 == 1:
#    print('Operação feita com sucesso, valor de pagamento: meticais')
# while opcao == 1:
 #      print('Operação feita com sucesso, valor de pagamento foi: {} mts'.format(d1))
# while opcao == 2:
  #     print('Operação feita com sucesso, valor de pagamento foi: {} mts'.format(d2))
# while opcao == 3:
 #      print('Operação feita com sucesso, valor de pagamento foi: {} mts'.format(d3))
# while opcao == 4:
  #     print('Operação feita com sucesso, valor de pagamento foi: {} mts'.format(d4))
# while opcao == 5:
   #    print('Operação feita com sucesso, valor de pagamento foi: {} mts'.format(d5))
# while opcao == 6:
    #   print('Operação feita com sucesso, valor de pagamento foi: {} mts'.format(d6))
# if opcao2 == 2:
#    print('Operação feita cancelada com sucesso, valor de pagamento foi de,',0,'mts')

