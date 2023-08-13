from math import radians, sin, cos, tan
# o ângulo precisa ser convertido para radianos
ang = float(input('Digite o ângulo que você deseja: '))
print(f'O ângulo de {ang:.2f}º tem o SENO de {sin(radians(ang)):.2f}º')
print(f'O ângulo de {ang:.2f}º tem o COSSENO de {cos(radians(ang)):.2f}º')
print(f'O ângulo de {ang:.2f}º tem a TANGENTE de {tan(radians(ang)):.2f}º')
