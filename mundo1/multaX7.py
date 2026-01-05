km = float(input('Você passou pelo radar com quantos km? '))
kmPassado = km - 80
if km > 80:
    print('Você foi multado no valor de ', kmPassado * 7, ' reais!')
else:
    print('Você não foi multado, continue assim!')