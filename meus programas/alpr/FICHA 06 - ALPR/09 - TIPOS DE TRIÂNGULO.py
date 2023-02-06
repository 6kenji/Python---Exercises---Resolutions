a = eval(input('Insira o lado a: '))
b = eval(input('Agora o lado b: '))
c = eval(input('Agora insira o lado c: '))
if a == b == c:
    print('Triângulo equilátero')
elif a == b or a == c or b == c:
    print('Triângulo escaleno')
elif a != b != c:
    print('Triângulo isósceles')
