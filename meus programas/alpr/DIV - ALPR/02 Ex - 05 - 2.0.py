"""
Um palíndromo é uma sequência de caracteres cuja leitura é idêntica se feita da
direita para esquerda ou vice−versa. Por exemplo: OSSO e OVO são palíndromos.
Em textos mais complexos os espaços e pontuação são ignorados. A frase SUBI NO
ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados.
Faça um programa que leia uma sequência de caracteres, mostre−a e diga se é um
palíndromo ou não.
"""
def palindromo(frase):
    inversor = ''
    espacos = " "
    for k in range(len(frase)-1,-1,-1):
        inversor = inversor + frase[k]
        if frase[k] == " ":
            espacos = espacos + 1
            p = espacos + 1
            if frase == inversor[p]:
                return True
            else:
                return False
frase = str(input('Insira uma sequência de caracteres: '))
print('Estado da verificação: ',palindromo(frase))
