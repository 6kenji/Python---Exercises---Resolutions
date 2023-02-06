"""
Dada uma cadeia de caracteres com uma frase informada pelo usuário (incluindo espaços em branco), escreva um programa que
contém:
 Os espaços em branco existem na frase.
 Quantidade de vezes que as vogais a, e, i, o, u aparecem.
"""
def frase_vogal_espaco(frase):
    vogal = 0
    contar_espaco = 0
    for k in frase:
        if k in "aeiou" or k in "AEIOU":
            vogal = vogal + 1
    print('A frase tem', vogal, 'vogais.')
    for k in frase:
        if " " in k:
            contar_espaco = contar_espaco + 1
    print('A frase tem', contar_espaco, 'espaço(s) em branco.')
frase = str(input('Insira uma frase qualquer: '))
frase_vogal_espaco(frase)