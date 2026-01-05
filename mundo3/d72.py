numeroMostrado = 0
num = str(input('Digite um valor inteiro entre 0 e 20: '))
if num.isnumeric() and int(num) >= 0 and int(num) <= 20:
    num = int(num)
else:
    while not num.isnumeric() or int(num) > 20 or int(num) < 0:
        num = str(input('Você digitou um valor inválido! Digite novamente usando números inteiros entre 0 e 20: '))
num = int(num)
numL = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezeseis', 'Desesete', 'Dezoito', 'Dezenove', 'Vinte')
numeroMostrado = numL[num]
print(f'Você digitou {num}')
print(f'Por extenso será {numeroMostrado}')