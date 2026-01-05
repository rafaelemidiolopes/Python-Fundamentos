def fatorial(num, show): 
    total = num
    if show == 'S':
        print(f'{num}', end=' ')
        for c in range(num-1, 0, -1):
            print(f'x {c}', end=' ')
            total *= c
        print(f'= {total}')
    elif show == 'N':
        for c in range(num-1, 0, -1):
            total *= c
        print(total)
fatorial(int(input('Qual número inteiro você deseja que seja faturado? ')), input('Você deseja ver os cálculos? [S]/[N]').strip().upper()[0])
