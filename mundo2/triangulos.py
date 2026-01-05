reta1 = float(input('Digite o número da primeira reta do triângulo: '))
reta2 = float(input('Digite o número da segunda reta do triângulo: '))
reta3 = float(input('Digite o número da última reta do triângulo: '))

if reta1 == reta2 and reta2 == reta3:
    print('O triângulo é equilátero!')
elif reta1 == reta2 or reta2 == reta3 or reta1 == reta3:
    print('O triângulo é isósceles!')
elif reta1 != reta2 and reta1 != reta3 and reta3 != reta2:
    print('O triângulo é escaleno!')