"""
Escreva uma função, com nome eliminar vogais, que aceita uma string como
parâmetros e retorna a mesma string sem vogais. Por exemplo, o chamado a função
eliminar vogais(“obrigado”) deverá retornar ”brgd”.
"""
def eliminar_vogais(string):
    nova_string = ''
    for k in string:
        if k not in "aeiou" and "AEIOU":
            nova_string = nova_string + k
    print('A nova string sem vogais é', nova_string)
string = str(input('Insira uma string com vogais: '))
eliminar_vogais(string)