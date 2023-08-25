from math import hypot
catop = float(input('Qual o comprimento do cateto oposto? '))
catad = float(input('Qual o comprimento do cateto adjacente? '))
hip = hypot(catop, catad)
print(f'O comprimento da hipotenusa é {hip:.2f}.')

    # O COMANDO PRINT TAMBÉM PODE SER FEITO DA SEGUINTE FORMA:
    # hip = (catop ** 2 + catad ** 2) ** (1 / 2)
    # print(f'O comprimento da hipotenusa é {hip:.2f}.')
