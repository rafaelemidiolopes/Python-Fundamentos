import sys
termo1 = (input('Digite o primeiro termo da progressão aritmética em número inteiro: '))
if termo1.isnumeric():
    termo1 = int(termo1)
else:
    print('Valor inválido. Reinicie o programa!')
razao = input('Digite a razão em número inteiro: ')
if razao.isnumeric():
    razao = int(razao)
else:
    print('Valor inválido. Reinicie o programa!')
    exit()
x = termo1 + (10-1) * razao
for c in range (termo1, x+1, razao):
    c
    print(c)