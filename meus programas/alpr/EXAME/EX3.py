"""
Pretende-se saber a distribuição percentual dos votos pelas 3 zonas do país. Os votos são
informados através dos números: 1 – para zona norte, 2 – para zona centro, 3 – para zona sul, 4
– para os votos nulos, 5 – para os votos em branco e 6 - ver estatísticas por zona.
Escreva um algoritmo (fluxograma, Python) que permitirá ler os votos das diferentes zonas.
Quando o operador seleccionar para visualizar as estatísticas por zona, o sistema deverá
imprimir a percentagem dos votos por zona assim como a percentagem de votos em branco e a
dos votos nulos, relativamente ao total dos votos.
"""
print('Bem vindo ao sistema nacional de votos! ')
print('1 – Zona norte')
print('2 – Zona centro')
print('3 – Zona sul')
print('4 – Votos nulos')
print('5 – Votos em branco')
print('6 - Estatísticas por zona')
opcao = eval(input('Agora insira uma opção para verificação: '))
if opcao == 1:
    percentagem_1 = 40 - (40/100)
    print('A percentagem da zona norte é de', percentagem_1,'%')
elif opcao == 2:
    percentagem_2 = 80 - (80/100)
    print('A percentagem da zona centro é de', percentagem_2,'%')
elif opcao == 3:
    percentagem_3 = 70 - (70/100)
    print('A percentagem da zona sul é de', percentagem_3,'%')
elif opcao == 4:
    votos_nulos = 6 - (6/100)
    print('A percentagem dos votos nulos é de', votos_nulos,'%')
elif opcao == 5:
    votos_branco = 2 - (2/100)
    print('A percentagem dos votos em branco é de', votos_branco,'%')
elif opcao == 6:
    percentagem_1 = 40 - (40 / 100)
    percentagem_2 = 80 - (80 / 100)
    percentagem_3 = 70 - (70 / 100)
    votos_nulos = 6 - (6 / 100)
    votos_branco = 2 - (2 / 100)
    print('A percentagem da zona norte é de', percentagem_1, '% em relaco a 198 votos')
    print('A percentagem da zona norte é de', percentagem_2, '% em relaco a 198 votos')
    print('A percentagem da zona norte é de', percentagem_3, '% em relaco a 198 votos')
    print('A percentagem dos votos nulos é de', votos_nulos, '% em relaco a 198 votos')
    print('A percentagem dos votos em branco é de', votos_branco, '% em relaco a 198 votos')