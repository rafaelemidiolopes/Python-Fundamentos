num = str(input('Digite um valor em números inteiros: '))
valor = 1
if num.isnumeric():
    num = int(num)
else:
    while not num.isnumeric():
        print('Digite um valor em números inteiros! ')
        num = str(input('Novo valor: '))
num = int(num)
fatorial = num 
while fatorial > 0:
    valor *= fatorial
    fatorial -=1
print(valor)