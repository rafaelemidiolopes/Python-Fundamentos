soma = 0
for c in range(1, 7):
    num = (input('Digite um número inteiro: '))
    if num.isnumeric():
        num = int(num)
        if num % 2 == 0:
         soma += num
    else:
        print('Valor inválido! Reinicie o programa.')
print(f'A soma dos números pares que estão entre esses seis números é: {soma}')