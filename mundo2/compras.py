maisBarato = 0
preco = ''
produto = ''
totalPreço = 0
decisão = ''
maisDe1000 = 0
contador = 0
nomeDoMaisbarato = ''
while True:
    print('='*30)
    print('    Cadastro de compras      ')
    print('='*30)
    produto = str(input('Digite o nome de um produto: ').lstrip())
    while not produto.isalpha():
        produto = str(input('Você digitou uma entrada inválida! Por favor, digite novamente usando apenas letras: ').lstrip())
    preco = str(input('Digite o valor do produto: ').strip())
    while not preco.isnumeric():
        preco = str(input('Você digitou um valor inválido! Por favor, digite novamente: ').strip())
    preco = float(preco)
    totalPreço += preco
    contador += 1
    if preco > 1000:
        maisDe1000 += 1
    if contador == 1:
        maisBarato = preco
        nomeDoMaisbarato = produto
    else:   
        if preco < maisBarato:
            maisBarato = preco
            nomeDoMaisbarato = produto
    decisão = str(input('você deseja continuar adicionando produtos? [S]/[N]').lower().strip())
    while decisão not in ['s', 'n']:
        decisão = str(input('Você digitou uma entrada inválida! Por favor, digite novamente usando "S" para continuar ou "N" para parar o programa: ').strip().lower())
    if decisão == 'n':
        break
print(f'O total gasto é de R${totalPreço}, {maisDe1000} produtos custam mais de 1000 reais e o produto mais barato é {nomeDoMaisbarato} custando R${maisBarato}')