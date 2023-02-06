"""
Faça um programa que para o tuplo (12, 3, 2, 5, 7, 30, 2, 4, 2, 1,13), ele imprime True
se o tuplo não contém números repetidos e False se tiver números repetidos
"""
def rep(Y):
    contar = 0
    for k in Y:
        contar = contar + 1
        if k in Y:
            if contar in Y and contar != k:
                return False
            else:
                return True
Y = (12, 3, 2, 5, 7, 30, 2, 4, 2, 1,13)
print('Verificando.... ',rep(Y))