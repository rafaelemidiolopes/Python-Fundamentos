mostrar = True
def fatorial(num, show): 
    total = num
    if show == 'S':
        """"
        No parâmetro show, caso ele seja falso, não mostrará o cálculo, caso seja verdadeiro, mostrará o cálculo
        no parâmetro return, retornará o valor total do cálculo"""
        print(f'{num}', end=' ')
        for c in range(num-1, 0, -1):
            print(f'x {c}', end=' ')
            total *= c
        print('= ', end='')
        return total
    elif show == 'N':
        global mostrar 
        mostrar = False
        for c in range(num-1, 0, -1):
            total *= c
        return total
total = fatorial(int(input('Qual número inteiro você deseja que seja faturado? ')), input('Você deseja ver os cálculos? [S]/[N]').strip().upper()[0])
if mostrar == True:
    print(total)
else:
    print(total)