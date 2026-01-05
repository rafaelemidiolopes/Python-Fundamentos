soma = contador = 0
while True:
    num = str(input('Digite um valor usando apenas números inteiros: '))
    if num.isnumeric():
        num = int(num)
    else:
        while not num.isnumeric():
            num = str(input('Você digitou um valor inválido! Por favor, use apenas números inteiros: '))
        num = int(num)
    soma += num
    contador +=1
    if num == 999:
        break
print(f'Você digitou {contador} valores, e a soma entre todos os valores é {soma}! ')