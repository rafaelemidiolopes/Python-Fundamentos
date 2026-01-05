VarControle = True
num = 0
maior = 0
menor = 0
média = 0
contador = 0

while VarControle == True:
    num = str(input('Digite um valor usando apenas números inteiros: '))
    if num.isnumeric():
        num = int(num)
    else:
        while not num.isnumeric():
            num = str(input('Você digitou um valor inválido! Digite novamente usando apenas valores em números inteiros: '))
        num = int(num)
    média += num
    if contador == 1:
        menor = num
        maior = num
    contador += 1
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    resp = str(input('Você deseja continuar adicionando novos valores? [S]/[N]').strip().upper())
    if resp != 'N' and resp != 'S':
        while resp != 'N' and resp != 'S':
            resp = str(input('Você digitou uma entrada inválida! Por favor, digite "S" para sim e "N" para não. ').strip().upper())
    if resp == 'S':
        VarControle = True
    elif resp == 'N':
        VarControle = False
média = média / contador
print(f'O menor valor é {menor}, o maior é {maior} e a média entre todos é {média:.2f}! ')
