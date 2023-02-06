"""
Faça um programa que para uma frase, apresente na tela as palavras que compõem essa frase.
Exemplo para a frase “Pedro, Paulo e Maria” apresente na tela:
Pedro
Paulo
Maria
"""
def separador(frase):
    sep = ' ' and 'aeiouAEIOU' and ','
    for n in frase:
        if n in frase:
            n = frase.split()
            if sep in frase:
                break
    print(n[0])
    print((n[len(n) - 1 - 2]))
    print((n[len(n) - 1]))
frase = input('Insira uma frase qualquer com nomes: ')
separador(frase)