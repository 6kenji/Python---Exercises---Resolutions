numero = eval(input('Insira o número da sua conta: '))
saldo = eval(input('Insira o saldo desta conta: '))
print('1.Depósito')
print('2.Retirada')
operacao = int(input('Que operação deseja fazer? '))
if operacao >= 3:
   print('Opção inválida!')
if operacao == 1:
   deposito = float(input('Quanto deseja depositar? '))
   ndeposito = saldo + deposito
   print('O seu saldo actual é de {} meticais'.format(ndeposito))
elif operacao == 2:
   retirada = float(input('Quanto deseja retirar? '))
   nretirada = saldo - retirada
   print('O seu saldo actual é de {} meticais'.format(nretirada))