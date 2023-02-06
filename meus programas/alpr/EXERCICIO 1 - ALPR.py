altura=eval(input("Insira a sua altura em metros(cm): "))
if altura > 178:
    peso1=(72.7*altura)-58
    print('O seu peso ideal é:', peso1, 'kilos')
elif altura < 178:
    peso2=(62.1 * altura)-44.7
    print('O seu peso ideal é:',peso2, 'kilos')
