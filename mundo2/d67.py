num = None
print('Olá! Este é um programa de tabuada.')
while True:
    num = str(input('Digite um valor inteiro que terá a tabuada dele mostrada até o 10. Digite um número negativo se desejar encerrar o programa. ').strip())
    if num.lstrip('-').isnumeric():
        num = int(num)
    else:
        while not num.lstrip('-').isnumeric():
            num = str(input('Você digitou um valor inválido! Digite novamente usando apenas números inteiros. Digite um número negativo se desejar encerrar o programa. ').strip())
        num = int(num)
    if num < 0:
        break
    print(f'A tabuada de {num} é:\n{num} X 1 = {num*1}')
    print(f'{num} X 2 = {num*2}')
    print(f'{num} X 3 = {num*3}')
    print(f'{num} X 4 = {num*4}')
    print(f'{num} X 5 = {num*5}')
    print(f'{num} X 6 = {num*6}')
    print(f'{num} X 7 = {num*7}')
    print(f'{num} X 8 = {num*8}')
    print(f'{num} X 9 = {num*9}')
    print(f'{num} X 10 = {num*10}')