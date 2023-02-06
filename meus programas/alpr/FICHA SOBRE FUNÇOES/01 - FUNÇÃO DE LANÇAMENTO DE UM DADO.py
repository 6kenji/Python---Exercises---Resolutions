#Inportar funcoes do random para numeros aleatorios
from random import*
def dado ():
    for k in range(6):
        numero = randint(1,6)
        print(numero)
#Executar
dado()
