numeros = []
while True:
    num = int(input('Digite um valor usando apenas números inteiros: '))
    numeros.append(num)
    varControle = input('Você deseja continuar dicionando valores? [S]/[N] ').strip().upper()[0]
    if varControle == 'N':
        break
quant = len(numeros)
numeros.sort(reverse=True)
if 5 in numeros:
    print(f'Você digitou {quant} elementos, a ordem decrescente dos valores é {numeros} e o 5 está na lista')
else:
     print(f'Você digitou {quant} elementos, a ordem decrescente dos valores é {numeros} e o 5 não está na lista')