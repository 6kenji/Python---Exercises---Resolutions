def espacos_vogais(frase):
    vogal = 0
    espacos_vazios = 0
    for k in frase:
        if k in "aeiou" or k in "AEIOU":
            vogal = vogal + 1
    print('A frase possui {} vogais'.format(vogal))
    for k in frase:
        if k in " ":
            espacos_vazios = espacos_vazios + 1
    print('A frase possui {} espaços em branco'.format(espacos_vazios))
#Exexcução
frase = str(input('Insira uma frase completa: '))
espacos_vogais(frase)