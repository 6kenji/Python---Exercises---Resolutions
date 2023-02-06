"""
Faça um programa que:
 Leia o nome;
 Leia o sobrenome;
 Concatene o nome com o sobrenome;
 Apresente o nome completo.
"""
def nome_completo(nome, sobrenome):
    con = nome + ' ' + sobrenome
    print('O seu nome completo é:', con)
nome = str(input('Insira o seu nome: '))
sobrenome = str(input('Insira o seu sobrenome: '))
nome_completo(nome, sobrenome)
