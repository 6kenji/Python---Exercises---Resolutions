nome=str(input('Insira o seu nome: '))
print('Seja bem vindo {} a plataforma online de venda de artigos!!'.format(nome))
print('1.Artigos de desporto, desconto de 28% - Preço 2350 mts')
print('2.Artigos de moda, desconto de 10% - Preço 350 mts')
print('3.Artigos de religião, desconto de 15% - Preço 3350 mts')
print('4.Artigos científicos, desconto de 45% - Preço 150 mts')
artigo=int(input('Qual artigo irá levar? '))
quantidade=int(input('Quantos irá levar '))
desconto1=(2350*quantidade)*0.28
desconto2=(350*quantidade)*0.1
desconto3=(3350*quantidade)*0.15
desconto4=(150*quantidade)*0.45
if artigo==1:
    print('{}, os artigos de desporto custam 2350 mts, o preço a ser pago é de: {} mts '.format(nome, desconto1))
if artigo==2:
    print('{}, os artigos de moda custam 350 mts, o preço a ser pago é de: {} mts '.format(nome, desconto2))
if artigo==3:
    print('{}, os artigos de religião custam 3350 mts, o preço a ser pago é de: {} mts '.format(nome, desconto3))
if artigo==4:
    print('{}, os artigos científicos custam 150 mts, o preço a ser pago é de: {} mta'.format(nome, desconto4))









