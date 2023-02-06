#Sempre que quiser usar este programa, deverá modificar os valores da variável k:
for k in range (5):
    print('Estudante',(k+1))
    teste1 = eval(input('Insira a nota do primeiro teste: '))
    teste2 = eval(input('Insira a nota do segundo teste: '))
    teste3 = float(input('Insira a nota do terceiro teste: '))
    media = (teste1 + teste2 + teste3) / 3
    if media >= 14:
        print('Estudante dispensado com média {}'.format(media))
    elif media >= 10:
        print('Estudante admitido ao exame com média {}'.format(media))
    else:
        print('Estudante excluído com média {}'.format(media))
