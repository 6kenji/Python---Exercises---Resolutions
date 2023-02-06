cateto_1 = eval(input('Insira o valor do cateto oposto: '))
cateto_2 = eval(input('Agora insira o valor do cateto adjacente: '))
hipotenusa = ((cateto_1**2) + (cateto_2**2))**(1/2)
print('A hipotenusa é igual a {:.2f}'.format(hipotenusa))
