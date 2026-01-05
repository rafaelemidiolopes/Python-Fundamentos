import random
num = int(random.randint(1, 5))
escolha = int(input('O computador pensou em um número inteiro entre 1 e 5. Tente adivinhar qual número é: '))
print ('Meus parabéns. Você acertou!' if escolha == num else 'Você errou. O computador pensou em {} Tente novamente.'.format(num))