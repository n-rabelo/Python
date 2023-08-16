dist = float(input('Qual é a distância da viagem? '))
print(f'Você está prestes a começar uma viagem de {dist:.2f} Km')
if dist > 200:
    print(f'E o preço da sua passagem será de R${dist * 0.45:.2f}')
else:
    print(f'E o preço da sua passagem será de R${dist * 0.5:.2f}')

# outra forma de fazer

dist = float(input('Qual é a distância da viagem? '))
print(f'Você está prestes a começar uma viagem de {dist:.2f} Km')
if dist <= 200:
    preco = dist * 0.50
else:
    preco = dist * 0.45
print(f'E o preço da sua passagem será de R${preco:.2f}')
