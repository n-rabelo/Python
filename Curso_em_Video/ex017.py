from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
#hip = (co ** 2) ** (1 / 2)
print(f'A hipotenusa vai medir {hypot(co, ca):.2f}')

