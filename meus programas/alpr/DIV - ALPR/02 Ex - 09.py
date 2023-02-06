"""
Crie uma função que recebe, como parâmetro, uma cadeia de caracteres e imprima
somente a última palavra da mesma. Se a se a cadeia de caracteres for “Instituto
Superior de Transportes e Comunicação ISUTC”, deverá ser impresso na tela a subcadeia “ISUTC”
"""
def parametro(p):
    palavra = ''
    frase = ''
    for i in range(len(p) - 1, 0, -1):
        palavra = palavra + p[i]
        if p[i] == ' ':
            break
    k = len(palavra) - 1
    while k >= 0:
        frase = frase + palavra[k]
        k = k - 1
    print(frase)
p = input('Insira um parâmetro para sua impressão: ')
parametro(p)