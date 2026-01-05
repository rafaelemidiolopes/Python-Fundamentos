num = str(input('Digite um valor em números inteiros que será fatorado: '))
if num.isnumeric():
    num = int(num)
else:
    while not num.isnumeric():
        print('ERRO!')
        num = str(input('Digite o valor apenas em números inteiros: '))
    num = int(num)
fatorial = 1
for c in range(num, 0, -1):
    fatorial  *= num
    num -=1
print(fatorial)