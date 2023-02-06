K = [2,4,23,1,76,3,36]
maior_valor = 0
for k in range(len(K)):
    if K[k] > maior_valor:
        maior_valor = K[k]
print(maior_valor)
