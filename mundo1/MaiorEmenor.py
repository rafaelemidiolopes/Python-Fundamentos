n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite o último número: '))
maior = n1
menor = n2

#maior
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3

#menor abaixo
if n1 < n2 and n1 < n3:
    menor = n1
if n3 < n2 and n3 < n1:
    menor = n3

print(f'O maior número é {maior} e o menor número é {menor}')