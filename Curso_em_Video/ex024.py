cidade = str(input('Em que cidade você nasceu? ')).strip().lower()
print('santo' in cidade)  # solução 1
print(cidade[:5] == 'santo')  # solução 2
