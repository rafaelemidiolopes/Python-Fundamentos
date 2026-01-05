numeros = []
contador = 0
for c in range(1,6):
    contador +=1
    num = int(input('Digite um valor usando apenas números inteiros: '))
    if contador == 1 or num > numeros[-1]:
        numeros.append(num)
    else:
        for indice, valor in enumerate(numeros):
            if valor >= num:
                numeros.insert(indice, num)
                break
print(f'Os números digitados em ordem crescente são: {numeros}')