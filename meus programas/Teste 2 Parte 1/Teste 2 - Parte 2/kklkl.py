""" Faça um programa baseado em funções:
que através de dois tuplo com dados inseridos pelo usuário,
ele cria um novo tuplo com os dados dos dois tuplos com os valores ordenados de forma decrescente.
"""
def decrescente(K):
    T1 = []
    tuplo_elementos = eval(input("Insira o numero de elementos que tuplo 1 deve ter: "))
    for i in range(tuplo_elementos):
        elemento = eval(input("Insira um valor do tuplo: "))
        T1.append(elemento)
    print(T1)
    tuplo_elementos2 = eval(input("Insira o numero de elementos que tuplo 2 deve ter: "))
    for j in range(tuplo_elementos2):
        elemento = eval(input("Insira um valor do tuplo: "))
        T2.append(elemento)
    print(T2)
    Y = (T1, T2)
    return Y
def ordem(Y):
    for s in range(len(Y)):
        for k in range(len(Y[s])):
            for i in range(k + 1, len(Y[s])):
                if Y[k] < Y[i]:
                    auxiliar_tuplo = Y[k]
                    Y[k] = Y[i]
                    Y[i] = auxiliar_tuplo
                    print('Ordenada: ', Y)
T1 = []
T2 = []
Y = (T1, T2)
decrescente(Y)