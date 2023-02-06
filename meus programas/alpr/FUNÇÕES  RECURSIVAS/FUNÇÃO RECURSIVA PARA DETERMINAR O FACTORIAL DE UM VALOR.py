def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial (n-1)

#EXECUÇÃO
n = eval(input('Insira um valor qualquer: '))
factorial(n)
print('O factorial de',n,'é igual a',factorial(n))