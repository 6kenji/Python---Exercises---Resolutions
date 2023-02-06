print('Insira o seu nome completo para verificar se é um Safar ou não... ')
nome = str(input()).strip()
print('Verificando....')
print('SAFAR' in nome.upper() or 'safar' in nome.lower())

