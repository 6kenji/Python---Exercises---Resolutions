"""
Crie uma função que permita contar o número de ocorrências de uma palavra em
uma frase. Exemplo: a frase “ana” está presente 4 vezes na frase “banana, mariana, e
Diana”
"""
def ocorencia (palavra,frase):
    contar = 0
    p = 0
    for k in palavra:
        if k in palavra and k in frase:
            contar = contar + 1
        p = contar + 1
    print('A palavra "',palavra,'" está repetida ', p, 'vezes')
palavra = input('Insira uma palavra referência: ')
frase = input('Agora insira uma frase: ')
ocorencia (palavra,frase)

