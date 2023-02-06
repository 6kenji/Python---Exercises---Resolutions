import random
def sorteio():
    for k in range(5):
        numeros_obtido1 = random.randint(1,49)
        numeros_obtido2 = random.randint(1,49)
        numeros_obtido3 = random.randint(1,49)
        numeros_obtido4 = random.randint(1,49)
        numeros_obtido5 = random.randint(1,49)
    bonus = random.randint(1,9)
    print('Os números sorteados sao:')
    K = [numeros_obtido1, numeros_obtido2, numeros_obtido3, numeros_obtido4, numeros_obtido5]
    print(K)
    print('Com o bonus de: ', bonus)
    s = bonus
    Y = [numeros_obtido1, numeros_obtido2, numeros_obtido3, numeros_obtido4, numeros_obtido5, s]
    print(Y)
sorteio()