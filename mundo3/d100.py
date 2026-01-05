import random
numeros = []
def sorteia():
    for c in range(0, 5):
        numeros.append(random.randint(0, 10))
    print('Sorteando os valores... \nPronto ->', end=' ')
    for c in numeros:
        print(f'{c}', end=' ')
    print()
def somaPar():
    soma = 0
    for c in numeros:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de {numeros}, temos {soma}!')
sorteia()
somaPar()