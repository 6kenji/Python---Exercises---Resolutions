def ordem_crescente(K):
# n = eval(input('Quantos números deseja inserir?: '))
#for k in range(n)
#print('Número: ', (k + 1))
#K = [n]
#print(K)
    for k in range(len(K)):
        for i in range(k + 1, len(K)):
            if K[k] > K[i]:
                auxiliar = K[k]
                K[k] = K[i]
                K[i] = auxiliar
    return K
K = [5,2,4,1,0,9,8]
print('Original: ',K)
print('Ordenada: ',ordem_crescente(K))
