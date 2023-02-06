lar = eval(input('Diga qual é a largura da parede em metros(m): '))
alt = eval(input('Agora a sua largura em metros(m): '))
area = lar * alt
if area >= 2:
    tinta_nec = area / 2
    print('Para uma parede de {} × {} que tem {} m² é necessário {} litros de tinta.'.format(lar,alt,area,tinta_nec))
else:
    print('Espaço insuficiente!')
