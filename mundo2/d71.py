import sys
print('='*30)
print('CAIXA ELETRÔNICO')
print('='*30)
nota50 = nota20 = nota10 = nota5 = nota2 = nota100 = 0 
valor = str(input('Quantos reais você deseja sacar? R$'))
if valor.isnumeric():
        valor = int(valor)
else:
        while not valor.isnumeric():
            valor = str(input('Você digitou um valor inválido! Por favor, digite novamente usando apenas números inteiros: R$'))
        valor = int(valor)
valorinicial = valor
if valor == 1:
        while valor == 1:
                valor = str(input('Não é possível sacar o valor de 1 real! Tente sacar outro valor: R$'))
                if valor.isnumeric():
                        valor = int(valor)
        else:
                while not valor.isnumeric():
                        valor = str(input('Você digitou um valor inválido! Por favor, digite novamente usando apenas números inteiros: R$'))
        valor = int(valor)
while valor // 100 >= 1:
        nota100 += 1
        valor -= 100
while valor // 50 >= 1:
        nota50 += 1
        valor -= 50
while valor // 20 >= 1:
        nota20 += 1
        valor -= 20
while valor // 10 >= 1:
        nota10 += 1
        valor -= 10
while valor // 5 >= 1:
        nota5 += 1
        valor -= 5
while valor // 2 >= 1:
        nota2 += 1
        valor -= 2
if valor == 1:
        print('Não foi possivel realizar o saque, pois sobrará o valor de 1 real. Por favor, reinicie o programa e tente novamente')
        sys.exit()
print(f'Você sacou R${valorinicial} reais. Foi preciso usar {nota100} notas de 100, {nota50} notas de 50, {nota20} notas de 20, {nota10} notas de 10, {nota5} notas de 5 e {nota2} notas de 2! ')