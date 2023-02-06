nome=str(input('Insira o seu nome: '))
print('Ola {}, abaixo temos a lista de nossos produtos e seus descontos: '.format(nome))
print('1.Porcas, desconto de 10%, e custam 509 mts cada: ')
print('2.Parafusos, desconto de 20%, e custam 350 mts cada: ')
print('3.Aurrelas, desconto de 30% e custam 600 mts cada. ')
opcao=int(input('Quais peças vai desejar?'))
opcao2=int(input('E o outro tipo?'))
opcao3=eval(input('Quanto ao terceiro tipo?'))
quantidade=eval(input('Quantas vai desejar da primeira escolhida??'))
quantidade2=eval(input('E outra quantidade?'))
quantidade3=int(input('E a terceira?'))
#///////
d1=((quantidade*509)*0.1)
pagamento1=((quantidade*509)-509)*0.1
#///////
d2=((quantidade2*350)*0.2)
pagamento2=((quantidade2*350)-350)*0.2
#///////
d3=((quantidade3*600)*0.3)
pagamento3=((quantidade3*600)-600)*0.3
if opcao==1 and 2:
    print('A(s) porca(s) tem desconto de {}, e o preço a ser pago é:{}, e o(s) parafuso(s) tem desconto de {}, e o preço a ser pago é:{} '.format(d1,pagamento1,d2,pagamento2))
elif opcao==2 and 3:
    print('O(s) parafuso(s) tem desconto de {}, e o preço a ser pago é:{}, e a(s) aurrelas(s) tem desconto de {}, e o preço a ser pago é:{} '.format(d2,pagamento2,d3,pagamento3))
elif opcao==3 and 1:
    print('A(s) aurrelas(s) tem desconto de {}, e o preço a ser pago é:{}, a(s) porca(s) tem desconto de {}, e o preço a ser pago é:{} '.format(d3,pagamento3, d1,pagamento1))


