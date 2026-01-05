r1 = float(input('Digite o valor da primeira reta '))
r2 = float(input('Digite o valor da segunda reta '))
r3 = float(input('Digite o valor da terceira reta '))
r1r2 = r1 + r2
r1r3 = r1 + r3
r2r3 = r2 + r3
if r1r2 > r3 and r1r3 > r2 and r2r3 > r1:
    print('Sim, é possivel fazer um triângulo!')
else:
    print('Não é possivel fazer um triângulo!')