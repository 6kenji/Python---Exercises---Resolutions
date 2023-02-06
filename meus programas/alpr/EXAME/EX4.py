"""
Escreva um programa que lê um conjunto de nomes (a inserção só para quando o utilizador
insere o nome “stop”), guarda em uma lista e imprime os nomes em que o número de vogais é
igual ao número de consoantes.
"""
s = "stop"
K = []
contar = 0
vogais = "aeiouAEIOU"
consoantes = "BCDFGHJKLMNPQRSTVXYZbcdfghjklmnpqrstvxyz"
nome = input('Insira um nome qualquer: ')
if nome == s:
    print('Parado com sucesso!',K[nome])
else:
    K.append(nome)
    nome = input('Insira outro nome: ')
for i in range(len(K)):
    ocoCons = 0
    ocoVogs = 0
    nome = K[i]
for letra in nome:
    if letra in consoantes:
       ocoCons = ocoCons + 1
    elif letra in vogais:
       ocoVogs = ocoVogs + 1
    while ocoCons == ocoVogs:
        ocoVogs = ocoCons
        indicador = i
print('O nome com vogais em igual número de consoantes  é ',indicador)