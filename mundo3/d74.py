import random
num1 = random.random()
num2 = random.random()
num3 = random.random()
num4 = random.random()
num5 = random.random()
numeros = (num1, num2, num3, num4, num5)
maior = max(numeros)
menor = min(numeros)
print('Os números gerados são:')
for num in numeros:
    print(num)
print(f'O menor número é: {menor} e o maior número é {maior}!')