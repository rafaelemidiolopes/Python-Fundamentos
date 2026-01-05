soma = int(0)
for c in range(1, 500+1, 2):
    if c % 3 == 0:
        soma += c
print(f'O resultado dos números impares e múltiplos de 3 é: {soma}')