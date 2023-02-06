""" Faça um programa baseado em funções:
que através de dois tuplo com dados inseridos pelo usuário,
ele cria um novo tuplo com os dados dos dois tuplos com os valores ordenados de forma decrescente.
"""
def decrescente(Y):
    #K[0] = eval(input('Insira o primeiro valor do tuplo: '))
    #K[1] = eval(input('Insira o segundo valor do tuplo: '))
    #K[2] = eval(input('Insira o terceiro valor do tuplo: '))
    #K[3] = eval(input('Insira o quarto valor do tuplo: '))
    #K[4] = eval(input('Insira o quinto valor do tuplo: '))
    #Y1 = (K[0], K[1], K[2], K[3], K[4])
    for k in range(len(Y)):
        for i in range(k + 1, len(Y)):
            if Y[k] < Y[i]:
                auxiliar_tuplo = Y[k]
                Y[k] = Y[i]
                Y[i] = auxiliar_tuplo

Y = [1,2,6,5,4,3,8,9]
print('Original: ',Y)
print('Ordenada: ',decrescente(Y))
decrescente(Y)