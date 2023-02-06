"""
Escreve um programa que lê uma palavra, a inverte, duplica o primeiro e o ultimo
carácter
"""
def palavra_magica(palavra):
    letra = ""
    i = len(palavra) - 1
    while i >= 0:
        letra = letra + palavra[i]
        i = i - 1
    print(palavra[i] + letra + palavra[0])
palavra = str(input('Insira uma palavra qualquer: '))
palavra_magica(palavra)