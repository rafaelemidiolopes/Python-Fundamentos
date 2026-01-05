# Este script tem o propósito de calcular a hipotenusa de um triângulo retângulo
import math
catAd = int(input('digite o valor do cateto adjacente '))
catOp = int(input('digite o valor do cateto oposto '))
hipotenusa = math.sqrt(catOp**2 + catAd**2 ) 
print(f'a hipotenusa mede {hipotenusa:.2f}  ')