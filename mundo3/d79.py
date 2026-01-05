valores = []
numero = 0
varControle = True
while varControle == True:
    numero = int(input('Digite um valor usando apenas números inteiros: '))
    if numero in valores:
         print('Valor duplicado. não é possivel adicionar novamente! ')
    else:
        valores.append(numero)
    pergunta = str(input('Você deseja continuar? [S]/[N] ').upper())
    if pergunta == 'N':
        varControle = False
valores.sort()
print(f'Os valores dicionado em ordem crescente são: {valores}')