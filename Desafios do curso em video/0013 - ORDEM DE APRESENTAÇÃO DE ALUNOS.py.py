from random import shuffle
nome_1 = input('Insira o primeiro nome: ')
nome_2 = input('Insira o segundo nome: ')
nome_3 = input('Insira o terceiro nome: ')
nome_4 = input('Insira o quarto nome: ')
nomes_sorteados = [nome_1,nome_2,nome_3,nome_4]
shuffle(nomes_sorteados)
print('A ordem de apresentação é: {}'.format(nomes_sorteados))