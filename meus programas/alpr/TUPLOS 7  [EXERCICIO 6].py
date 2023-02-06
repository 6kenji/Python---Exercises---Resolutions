T = [12,3,2,5,7,30,2,4,2,1,13]
a = eval(input('Insira um valor: '))
vezes = 0
for k in range(len(T)):
    if a == T[k]:
        vezes = vezes + 1
print(vezes)
