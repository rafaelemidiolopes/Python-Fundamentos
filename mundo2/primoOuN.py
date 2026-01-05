num = input('Digite um número inteiro: ')
if num.isnumeric():
    num = int(num)
    contador = 0
    for c in range(1, num+1):
        if num % c == 0:
            contador += 1
else:
    print('Valor inválido. Reinicie o programa!')
    exit()
if contador == 2:
    print('O número é primo! ')
else:
    print('O número não é primo! ')