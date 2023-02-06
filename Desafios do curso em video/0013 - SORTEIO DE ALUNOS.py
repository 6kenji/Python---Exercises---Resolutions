import random
nome_1 = input('Insira o primeiro nome: ')
nome_2 = input('Insira o segundo nome: ')
nome_3 = input('Insira o terceiro nome: ')
nome_4 = input('Insira o quarto nome: ')
nome_sorteado = [nome_4,nome_3,nome_2,nome_1]
sorteio = random.choice(nome_sorteado)
print('O aluno {} foi o escolhido! '.format(sorteio))
