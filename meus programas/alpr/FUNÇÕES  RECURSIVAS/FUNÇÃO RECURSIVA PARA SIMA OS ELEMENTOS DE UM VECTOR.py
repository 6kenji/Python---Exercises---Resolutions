def soma(V, tamanho):
    if tamanho == 0:
        return 0
    else:
        return V[tamanho - 1] + soma(V, tamanho - 1)
#EXECUÇÃO
V = [2,5,4,3,4]
soma(V, len(V))
print('Soma =',soma(V, len(V)))
