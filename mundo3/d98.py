cont = 0
def contador (inicio, fim, passo):
    global cont 
    cont += 1
    if cont == 1:
        for c in range(inicio, fim, passo):
            print(c, end=' ')
        print()
    if cont == 2:
        for c in range(inicio, fim, passo):
            print(c, end=' ')
        print()
    if cont == 3:
        print(f'Contando de {inicio} até {fim+1} de em {passo} passos...')
        for c in range(inicio, fim, passo):
            print(c, end=' ')
        print()
if cont == 0:
    contador(0, 11, 1)
if cont == 1:
    contador(10, -1, -2)
if cont == 2:
    print('Hora de personalizar sua contagem! ')
    contador(int(input('Inicio: ')), int(input('Fim: ')), int(input('Passo: ')))
