def soma (teste_1,teste_2):
    s = teste_1 + teste_2
    return s
def media(teste_1,teste_2):
    m = soma(teste_1, teste_2) / 2
    print('A média é: {} valores'.format(m))
#Executar
teste_1=eval(input('Insira a nota do teste 1: '))
teste_2=eval(input('Insira a nota do teste 2: '))
media(teste_1, teste_2)