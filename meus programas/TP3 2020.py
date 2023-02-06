def soma_divisores (n,k = 1):
    sdp = 0
    if n == 1:
        return sdp + k
    else:
        if k <= n:
            if n % k == 0:
                return soma_divisores(n,k+1,sdp+1)
            elif n % 1 != 0:
                 return soma_divisores(n,k+1,sdp)
#EXECUTAR
n=eval(input('Insira um valor qualquer:'))
print('A soma dos divisores de {} e: {}'.format(n,soma_divisores(n)))


