"""
Crie uma função que recebe uma palavra, e essa função deverá criar uma nova
palavra que representa o espelho da palavra inicial.
Exemplo: ao inserir a palavra “python” teremos como saída “pythonnohtyp”. Ao
inserir “1234” teremos como saída “12344321” .
"""
def palavra_magica2(palavra):
    for i in palavra:
        for k in palavra:
            if i in palavra:
                i = palavra[::-1][0]
                k = palavra[::-1]
    print(palavra + k)
palavra = input('Insira uma palavra: ')
palavra_magica2(palavra)