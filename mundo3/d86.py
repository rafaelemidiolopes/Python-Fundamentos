matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
parSoma = somaTerceiraColuna = 0
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}] [{c}]: '))
        if matriz [l][c] % 2 == 0:
            parSoma += matriz [l] [c]
        if matriz [0][2] or matriz [1][2] or matriz [2][2] :
            somaTerceiraColuna += matriz [l][2]
        maiorValor2linha = matriz [1][0]
        if matriz[1][1] > maiorValor2linha:
            maiorValor2linha = matriz[1][1]
        if matriz[1][2] > maiorValor2linha:
            maiorValor2linha = matriz[1][2]
print(matriz[0])
print(matriz[1])
print(matriz[2])
print(f'A soma de todos valores pares é {parSoma}, a soma dos valores da terceira coluna é {somaTerceiraColuna} e o maior valor da segunda linha é {maiorValor2linha}! ')