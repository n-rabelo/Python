from random import randint
from time import sleep

computador = randint(0, 5)
print('-=' * 30)
print('Vou penar em um número entre 0 e 5. Tente advinhar...')
print('-=' * 30)
jogador = int(input('Em qual número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você consegiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {computador} e não no {jogador}')