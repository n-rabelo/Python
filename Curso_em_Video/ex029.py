veloc = float(input('Qual é a velocidade atual do carro? '))
if veloc > 80:
    multa = (veloc - 80) * 7
    print(f'MULTADO! Você excedeu o limite permitido que é de 80 km/h')
    print(f'Você deve pagar uma multa de R${multa:.2f}!')
print('Tenha um bom dia! Dirija com segurança')
