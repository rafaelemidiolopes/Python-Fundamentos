N = str(input('Digite um valor que será somados a outros valores utilizando apenas números inteiros: ').strip())
if N.isnumeric():
    N = int(N)
else:
    while not N.isnumeric():
        N = str(input('Valor inválido! Digite o valor usando apenas números inteiros: ').strip())
N = int(N)
Soma = int(N)
contador = 1
OutroValor = int(Soma)
while OutroValor != 999:
    contador +=1
    OutroValor = str(input('Digite outro valor usando apenas números inteiros, esses números serão somados e mostrará quantos números foram digitados.  Digite 999 se desejar parar: ').strip())
    if OutroValor.isnumeric():
        OutroValor = int(OutroValor)
    else:
        while not OutroValor.isnumeric():
            OutroValor = str(input('Valor inválido! Digite o valor usando apenas números inteiros: ').strip())
    OutroValor = int(OutroValor)
    if OutroValor == 999:
        break
    Soma += OutroValor
print(f'Foi digitado {contador} valores no total e {Soma} é a soma de todos valores!')
