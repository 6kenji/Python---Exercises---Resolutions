#Fazer um programa que determine a quantidade de vogais no nome completo de uma pessoa.
vogal = 0
nome = str(input('Insira um nome completo: '))
for k in nome:
    if k in "aeiou" or k in "AEIOU":
        vogal = vogal + 1
print('O nome {} possui {} vogais'.format(nome, vogal))
