def delta(a, b, c):
    d = b ** 2 - 4 * a * c
    return d
def raizesdafuncao(a, b, c):
    rf = d(a, b, c)
    if rf == 0:
        x = - b / 2 * a
        print('A função tem raíz dupla x1=x2 = {}'.format(x))
    elif rf > 0:
        x1 = (- b + rf ** (1 / 2)) / 2 * a
        x2 = (- b - rf ** (1 / 2)) / 2 * a
        print('x1={} e x2={}'.format(x1, x2))
    else:
        print('Não tem solução em R.')
#EXECUÇAO
a = eval(input('Insira o valor de a ...NB:O mesmo deve ser diferente de zero(0):'))
