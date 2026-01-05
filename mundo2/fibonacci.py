anterior2 = 0
anterior1 = 1
soma = 0
N = str(input('Digite um número que será referência para mostrar a quantidade de números da sequência de Fibonacci que você quiser: '))
if N.isnumeric():
    N = int(N)
else:
    while not N.isnumeric():
     N = str(input('Valor inválido! Digite o valor usando apenas números inteiros: '))
N = int(N)
contador = 0
while contador < N:
    print(f'{anterior2}')
    soma = anterior1 + anterior2
    anterior2 = anterior1
    anterior1 = soma
    contador +=1