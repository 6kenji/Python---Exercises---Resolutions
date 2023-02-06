"""
Faça um programa que para o tuplo (12, 3, 2, 5, 7, 30, 2, 4, 2, 1,13) lê um número, e
informa a posição da primeira ocorrência desse número. Caso o número não seja
encontrado deve ser impresso -1
"""
def ocorencia(num):
    pos = -1
    if num in S:
        for k in range(len(S)):
            if S[k] == num:
                if pos == -1:
                    pos = k + 1
        print('A posição da primeira ocorrência é: ',pos, '.Nota: Conta a partir de 1!')
    else:
        print('-1')
S = (12, 3, 2, 5, 7, 30, 2, 4, 2, 1,13)
print(S)
num = eval(input('Insira um número que deseja saber a sua posição da primeira ocorrência: '))
ocorencia(num)