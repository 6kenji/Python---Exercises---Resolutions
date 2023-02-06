"""
Crie uma função para ler uma frase e contar o número de palavras dessa frase.
Considere que as palavras estão separadas por espaços brancos ou vírgulas.
Exemplos:
“Processamento” contém 1 palavra. “Processamento da informação” contém 3 palavras.
“computador, caderno e caneta” contém  4 palavras. “” não contém palavras
"""
def contar_palavras(frase):
    contar = 0
    f = 0
    for k in range(len(frase)):
        if frase[k] == " ":
            contar = contar + 1
            f = contar + 1
    if f == 0:
        print('Não contém palavras')
    print('A frase acima contém ', f, 'palavra(s).')
frase = input('Insira uma frase: ')
contar_palavras(frase)