num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite um outro número inteiro: '))

maior = num1
menor = num2

if num1 < num2:
    maior = num2
    menor = num1
    print(f'O maior número é {maior} e o menor número é {menor}')
elif num1 == num2:
    print('Não existe número maior nem menor neste caso, pois os dois são iguais.')
else: 
    print(f'O maior número é {maior} e o menor número é {menor}')