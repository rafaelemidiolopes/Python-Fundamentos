frase = str(input('Digite uma frase: ').lower())
frase = frase.replace(' ', '')
if frase[0:] == frase[::-1]:
    print('A frase é polindromo! ')
else:
    print('A frase não é um polindromo! ')