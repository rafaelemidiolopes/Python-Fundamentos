num = int(input('Digite um número '))
#print(f'{num} é par' if num / 2 == 0 else f'{num} é impar')
if num % 2 == 0:
    print(f'{num} é par')
else:
    print(f'{num} é impar')