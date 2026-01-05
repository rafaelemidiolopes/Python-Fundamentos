import random
palpites = 1
num = int(random.randint(0, 10))
escolha = str(input('O computador pensou em um número inteiro entre 0 e 10. Tente adivinhar qual número é: '))
while not escolha.isnumeric(): ### enquanto n for numero, vai ficar dando valor invalido até for###
        escolha = str(input('Valor inválido! Digite um número inteiro entre 0 a 10: '))
escolha = int(escolha) ###aqui já passou daquele while de cima, ou seja, é um numero em uma string q vai virar um numero mesmo###
while escolha != num: ###aqui enquanto n for o numero certo, o palpite aumenta e recebe outra chance, mas aqui n tem while nenhum pra verificar se é um numero ou letra...###
    palpites += 1
    escolha = str(input('Você errou! Tente novamente: '))
    if escolha.isnumeric(): ###se for numero vira um numero sem ser string###
        escolha = int(escolha)
    else:
     while not escolha.isnumeric(): ###se n, enquanto n for numero, vai ficar dando valor invalido até for###
        escolha = str(input('Valor inválido! Digite um número inteiro entre 0 a 10: '))
escolha = int(escolha) ###aqui já passou daquele while de cima, ou seja, é um numero em uma string q vai virar um numero mesmo###
print (f'Meus parabéns. Você acertou! O número que o computador pensou foi {num} e foi necessário {palpites} palpites!')