anoNasc = int(input('Em qual ano você nasceu? '))
idade = 2025 - anoNasc
if 2025 - anoNasc < 18:
    tempoRestante = 18 - idade
    print(f'Você ainda não precisa se alistar! Porém falta {tempoRestante} anos para você poder se alistar ')
elif 2025 - anoNasc >= 18 and idade <= 45:
    print('Esta na hora de se alistar!')
else:
    tempoQpassou = idade - 18
    print(f'Já passou da hora de se alistar! Passou {tempoQpassou} anos ')
    