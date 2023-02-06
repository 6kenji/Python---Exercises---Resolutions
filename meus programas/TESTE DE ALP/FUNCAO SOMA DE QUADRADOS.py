#Soma dos quadrados dos números antecessores de n
#Khalidy Safar
def soma_quadrados():
    p = n-1
    soma = n**2 + (n-p)**2 + p**2
    print('A soma dos quadrados antecessores deste número é: {}'.format(soma))
#Executar
n = eval(input('Insira um número qualquer: '))
soma_quadrados()
