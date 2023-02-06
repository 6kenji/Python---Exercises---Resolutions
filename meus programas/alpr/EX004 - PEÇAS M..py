nome=str(input('Insira o seu nome: '))
print('Ola {}, abaixo temos a lista de nossos produtos e seus descontos: '.format(nome))
print('1.Porcas, desconto de 10%, e custam 509 mts cada: ')
print('2.Parafusos, desconto de 20%, e custam 350 mts cada: ')
print('3.Aurrelas, desconto de 30% e custam 600 mts cada. ')
opcao=int(input('Qual peça vai desejar?'))
quantidade=eval(input('Quantas vai desejar?'))
#///////
d1=((quantidade*509)*0.1)
pagamento1=((quantidade*509)-509)*0.1
#///////
d2=((quantidade*350)*0.2)
pagamento2=((quantidade*350)-350)*0.2
#///////
d3=((quantidade*600)*0.3)
pagamento3=((quantidade*600)-600)*0.3
if opcao==1:
    print('A(s) porca(s) tem desconto de {}, e o preço a ser pago é:{} '.format(d1,pagamento1))
elif opcao==2:
    print('O(s) parafuso(s) tem desconto de {}, e o preço a ser pago é:{} '.format(d2,pagamento2))
elif opcao==3:
    print('A(s) aurrelas(s) tem desconto de {}, e o preço a ser pago é:{} '.format(d3,pagamento3))



