def fibonacci(k):
    if k == 1:
        return 0
    elif k == 2:
        return 1
    else:
        return fibonacci(k - 2) + fibonacci(k - 1)
def soma_fibonacci(k):
    soma = 0
    for i in range(1,k + 1):
        soma = soma + fibonacci(i)
    print('O fibonacci de {} é {}'.format(k, soma))
k = eval(input("Escreve um valor para calcular o seu fibonnaci: "))
soma_fibonacci(k)
