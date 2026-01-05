valores = []
maior = 0
menor = 0
posmenor = []
posmaior = []
for c in range(0,5):
    valores.append(int(input(f'Digite um valor usando apenas números inteiros para a posição {c+1}: '))) 
    if c == 0:
        maior = valores[c]
        menor = valores[c]
    if maior < valores[c]:
        maior = valores[c]
    if  menor > valores[c]:
        menor = valores[c]
for indice, valor in enumerate(valores):
        if valor == maior:
            posmaior.append(indice+1)
        if valor == menor:
            posmenor.append(indice+1)
print(f'O menor valor digitado foi {menor} e o maior valor digitado foi {maior}, e suas respectivas posições são: {posmenor} e {posmaior}!')