"""
Escreva um programa que lê um conjunto de nomes (a inserção só para quando o utilizador
insere o nome “stop”), guarda em uma lista e imprime os nomes em que o número de vogais é
igual ao número de consoantes.
"""
L = []
nome = input('Insira um nome qualquer: ')
while nome!= "stop":
    L.append(nome)
    nome = input('Insira um outro nome: ')
    print(L)
for k in range(len(L)):
    nome = L[k]
    ocoVog = 0
    ocoCons = 0
for letra in nome:
    vogais = "aeiouAEIOU"
    consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    if letra in vogais:
        ocoVog = ocoVog + 1
    if letra in consoantes:
        ocoCons = ocoCons + 1
        if ocoVog == ocoCons:
           indicador = k
print('O nome com vogais em igual número de consoantes  é ',L[indicador])