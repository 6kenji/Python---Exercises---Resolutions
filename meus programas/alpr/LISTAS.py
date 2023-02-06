def par_impar(K):
    Kpar = []
    Kimpar = []
    for i in range (len(K)):
        if K[i] % 2 == 0:
            Kpar.append(K(i))
        else:
            Kimpar.append(K(i))
    print('Vector para números pares: {}'.format(Kpar))
    print('Vector para números impares: {}'.format(Kimpar))
#Execucao
K = [2,3,7,9,11,13,15,22]
print(K)
par_impar(K)
