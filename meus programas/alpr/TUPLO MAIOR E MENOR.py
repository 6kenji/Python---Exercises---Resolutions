"""
def maior_menor(K):
    menor = K[0]
    maior = K[len(K) - 1]
    for i in range(len(K)):
        if menor > K[i]:
            if maior < K[i]:
                menor = K[i]
                maior = K[i]
    print('Menor valor:',menor)
    print('Maior valor:',maior)
K = (10,15,3,2,4,0,15,9,78)
maior_menor(K)
#//////////////////////////////////////////////////////
"""
def preencher(n):
    K = []
    for i in range(n):
        valor = eval(input('Insira um valor:  '))
        K.append(valor)
    return K
def maior_menor(K):
    K = preencher(n)
    print(K)
    menor = K[0]
    maior = K[len(K)-1]
    encontrado = -1
    encontrado2 = -1
    for i in range(len(K)):
        for k in range(len(K)):
            if menor > K[i]:
                if maior < K[k]:
                    menor = K[i]
                    maior = K[i]
                encontrado = i
                encontrado2 = k
    aux = K[0]
    K[0] = menor
    aux2 = K[len(K)-1]
    K[len(K) - 1] = maior
    K[encontrado] = aux
    K[encontrado2] = aux2
    print(K)
n = eval(input('Insira o tamanho: '))
maior_menor(n)
#////////////////////////////////////////////////////////
