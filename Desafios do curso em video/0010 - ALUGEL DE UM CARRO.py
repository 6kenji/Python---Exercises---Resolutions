dias = eval(input('Informe os dias de uso do carro: '))
d = eval(input('Agora a distância percorida em km: '))
alugel = (dias * 60) + (d * 0.15)
print('O valor do alugel a ser pago é de {:.2f} meticais'.format(alugel))
