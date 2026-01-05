vezesnumero9 = 0
num1 = str(input('Digite o primeiro valor usando apenas números inteiros: '))
if not num1.isnumeric():
    while not num1.isnumeric():
        num1 = str(input('ERRO! Digite a entrada novamente usando apenas números inteiros: '))
        
num2 = str(input('Digite o segundo valor usando apenas números inteiros: '))
if not num2.isnumeric():
    while not num2.isnumeric():
        num2 = str(input('ERRO! Digite a entrada novamente usando apenas números inteiros: '))
        
num3 = str(input('Digite o terceiro valor usando apenas números inteiros: '))
if not num3.isnumeric():
    while not num3.isnumeric():
        num3 = str(input('ERRO! Digite a entrada novamente usando apenas números inteiros: '))

num4 = str(input('Digite o quarto e último valor usando apenas números inteiros: '))
if not num4.isnumeric():
    while not num4.isnumeric():
        num4 = str(input('ERRO! Digite a entrada novamente usando apenas números inteiros: '))
        
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
num4 = int(num4)

numeros = (num1, num2, num3, num4)
vezesnumero9 = numeros.count(9)
primeiro3 = numeros.index(3)

numerospares = 0

if num1 % 2 == 0:
    numerospares +=1
if num2 % 2 == 0:
    numerospares +=1
if num3 % 2 == 0:
    numerospares +=1
if num4 % 2 == 0:
    numerospares +=1
    
print(f'Os números digitados são: {num1}, {num2}, {num3} e {num4}. O número 3 apareceu primeiro na{primeiro3+1}º posição, o número 9 apareceu {vezesnumero9} vezes e você digitou {numerospares} números pares!')