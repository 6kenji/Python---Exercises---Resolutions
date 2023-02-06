"""
Faça um programa que permite atraves do teclado inserir uma frase/palavra e dois caracteres (velho e novo)
, sendo o caracter velho existente na frase/palavra e o caracter novo que deve substituir o caracter
velho na frase/palavra original
"""
def substituir(frase, sub_novo, sub_velho):
    nova = ''
    for k in range(len(frase)):
        if frase[k] == sub_velho:
            nova = nova + sub_novo
        else:
            nova = nova + frase[k]
    print(nova)
frase = input('Insira uma frase: ')
sub_velho = input('Insira um caracter velho para substituir: ')
sub_novo = input('Insira um caracter novo para substituir o velho: ')
substituir(frase, sub_novo, sub_velho)