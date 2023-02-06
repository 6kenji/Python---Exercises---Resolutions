T = (12,3,2,5,7,30,2,4,2,1,13)
k = eval(input('Insira um valor: '))
for k in range(len(T)):
    if k in T:
        print('A posição da primeira ocorrência e:',len(T))
    else:
        print(-1)
