num_pares = []
num_impares = []
for c in range(0,7):
    num = int(input('Digite um número usando apenas números inteiros: '))
    if num % 2 == 0:
        num_pares.append(num)
    else:
        num_impares.append(num)
num_impares.sort()
num_pares.sort()
numeros = (num_impares, num_pares)
print(f'Os números pares da lista em ordem crescente são: {numeros[1]}')
print(f'E os impares são: {numeros[0]}')