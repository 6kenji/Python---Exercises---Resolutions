ano=int(input('Escolha um ano: '))
if ano % 4 == 0 and ano % 100 != 0 :
    print('O ano de {} é bissexto'.format(ano))
else:
    print('O ano de {} não é bissexto'.format(ano))
