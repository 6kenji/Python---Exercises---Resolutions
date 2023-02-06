"""
Crie uma função que recebe duas palavras e retorne True caso a primeira palavra
seja um prefixo da segunda. Exemplo: “uf” é prefixo de “ufabc”. “ufabc” não é
prefixo de “uf”
"""
def prefixo(palavra_1, palavra_2):
    for k in palavra_1:
        if k in palavra_1 and palavra_1 in palavra_2:
            return True
        else:
            return False
palavra_1 = input('Insira a primeira palavra: ')
palavra_2 = input('Insira a segunda palavra: ')
print('Estado da verificação: ',-prefixo(palavra_1, palavra_2))
