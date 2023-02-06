def espacos(frase):
    vogal = 0
    for k in frase:
        if k in "aeiou" or k in "AEIOU":
            vogal = vogal + 1
    print('A frase possui {} vogais'.format(vogal))
    print('A frase possui {} espaços em branco'.format(frase.count(" ")))
#Exexcução
frase = str(input('Insira uma frase completa: '))
espacos(frase)