from math import sin, cos, tan, atan, acos, asin, radians, atan2
k = eval(input('Insira um ângulo qualquer: '))
seno = sin(radians(k))
cosseno = cos(radians(k))
tangente = tan(radians(k))
cotangente = atan(radians(k))
arcosseno = asin(radians(k))
arcocosseno = acos(radians(k))
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print('.'*20)
print('O seno de {} é {:.2f}'.format(k, seno))
print('O cosseno de {} é {:.2f}'.format(k, cosseno))
print('A tangente de {} é {:.2f}'.format(k, tangente))
print('A cotangente de {} é {:.2f}'.format(k, cotangente))
print('O arcosseno de {} é {:.2f}'.format(k, arcosseno))
print('O arcocosseno de {} é {:.2f}'.format(k, arcocosseno))