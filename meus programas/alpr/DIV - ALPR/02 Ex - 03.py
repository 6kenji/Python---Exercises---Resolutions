"""
Faça um programa que, a partir de um texto digitado pelo usuário, conte o número
de caracteres total e o número de palavras (palavra é definida por qualquer
sequência de caracteres delimitada por espaços em branco) e exiba o resultado
"""
def caracteres_palavras(frase):
    palavras = 0
    p = []
    for k in range(len(frase)):
        if frase[k] == " ":
            palavras = palavras + 1
            p = palavras + 1
    print('A frase tem', p, 'palavras.')
    caracteres = len(frase) - palavras
    print('A frase tem', caracteres, 'caracteres.')
frase = str(input('Insira uma frase qualquer: '))
caracteres_palavras(frase)
