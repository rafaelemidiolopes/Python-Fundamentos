anoNasc = int(input('Em qual ano você nasceu? '))
idade = 2025 - anoNasc

if idade <= 9:
    print('Sua categoria é mirim!')
elif idade <= 14:
    print('Sua categoria é infantil!')
elif idade <= 19:
    print('Sua categoria é júnior!')
elif idade <= 20:
    print('Sua categoria é sênior!')
else:
    print('Sua categoria é master!')