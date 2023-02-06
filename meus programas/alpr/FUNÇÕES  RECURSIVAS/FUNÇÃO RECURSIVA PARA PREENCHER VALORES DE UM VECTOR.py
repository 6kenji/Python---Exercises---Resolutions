T = []
n = eval(input('Insira o tamanho do seu vector: '))
for k in range (n):
    valor = eval(input('Insira um valor: '))
    T.append(valor)
print(T)
def soma(T, tamanho):
    if tamanho == 0:
        return 0
    else:
        return T[tamanho - 1] + soma(T, tamanho - 1)
#EXECUÇÃO
soma(T, len(T))
print('Soma =',soma(T, len(T)))