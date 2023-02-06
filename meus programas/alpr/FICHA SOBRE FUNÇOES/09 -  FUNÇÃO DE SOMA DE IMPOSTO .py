def soma_imposto(taxaImposto,custo):
    custo = 0
    venda = 0
    taxaImposto = 0
    valor_arrecadado = custo * venda
    taxaImposto = custo - custo * 0.015
    s = taxaImposto + custo
    print('O imposto sobre as vendas é de {} meticais'.format(s))
#Executar
custo = eval(input('Qual é o custo dos produtos de  venda: '))
valor_arecadado = eval(input('Insira o valor arrecadado nas suas vendas: '))
soma_imposto(taxaImposto,custo)
