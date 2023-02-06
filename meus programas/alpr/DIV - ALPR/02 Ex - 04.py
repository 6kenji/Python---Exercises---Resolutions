"""
Escreve um programa que lê uma palavra, a inverte, duplica o primeiro e o ultimo
carácter
"""
def palavra_magica(palavra):
    for i in palavra:
        for k in palavra:
            if i in palavra:
                i = palavra[::-1][0]
                k = palavra[::-1]
    print(i + k + palavra[0])
palavra = str(input('Insira uma palavra qualquer: '))
palavra_magica(palavra)
