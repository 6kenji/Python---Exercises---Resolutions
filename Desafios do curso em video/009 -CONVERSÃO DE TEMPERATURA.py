temperatura = eval(input('Insira um valor para a temperatura: '))
print('1.Celsius(ºC)')
print('2.Fahrenheit(ºF)')
print('3.Kelvin(ºK)')
#///////////////////////////////////
c_f = (temperatura * 1.8) + 32
f_c = 32 - (temperatura / 1.8)
#///////////////////////////////////
c_k = temperatura + 273.15
k_c = temperatura - 273.15
#///////////////////////////////////
k_f = (temperatura * 1.8) - 459.67
f_k = (temperatura + 459.67) / 1.8
#///////////////////////////////////
unidade = int(input('Qual é a sua unidade de medição? '))
if unidade == 1:
    print('1.Fahrenheit(ºF)')
    print('2.Kelvin(ºK)')
    unidade2 = eval(input(('Deseja mudar {} ºC para que outra unidade acima? '.format(temperatura))))
    if unidade2 == 1:
        print('{} ºC equivalem a {} ºF'.format(temperatura,c_f))
    elif unidade2 == 2:
        print('{} ºC equivalem a {} ºK'.format(temperatura,c_k))
elif unidade == 2:
    print('1.Celsius(ºC)')
    print('2.Kelvin(ºK)')
    unidade2 = eval(input(('Deseja mudar {} ºF para que outra unidade acima? '.format(temperatura))))
    if unidade2 == 1:
        print('{} ºF equivalem a {} ºC'.format(temperatura, f_c))
    elif unidade2 == 2:
        print('{} ºF equivalem a {} ºK'.format(temperatura, f_k))
elif unidade == 3:
    print('1.Celsius(ºC)')
    print('2.Fahrenheit(ºF)')
    unidade2 = eval(input(('Deseja mudar {} ºK para que outra unidade acima? '.format(temperatura))))
    if unidade2 == 1:
        print('{} ºK equivalem a {} ºC'.format(temperatura, k_c))
    elif unidade2 == 2:
        print('{} ºK equivalem a {} ºF'.format(temperatura, k_f))