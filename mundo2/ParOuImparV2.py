print('Este é um jogo de par ou ímpar! ')
vitoriasCons = 0
result = 0
import random
while True:
    num = str(input('Digite o número para jogar: '))
    if num.isnumeric():
        num = int(num)
    else:
        while not num.isnumeric():
            num = str(input('Você digitou um valor inválido! Digite novamente usando apenas números inteiros: '))
        num = int(num)
    Maquina = int(random.randint(0, 10000))
    Jogador = str(input('Você deseja escolher par ou ímpar? ').strip().lower())
    Jogador = Jogador.replace('í', 'i')
    if Jogador != 'impar' and Jogador != 'par':
        while Jogador != 'impar' and Jogador != 'par':
            Jogador = str(input('Você digitou uma entrada inválida. Por favor, digite "Impar" se desejar escolher impar, ou "par" para escolher par: ').strip().lower())
    result = num + Maquina
    if result % 2 == 0:
        if Jogador == 'impar':
            print(f'Você perdeu! O resultado foi de {result} e você ganhou {vitoriasCons} vezes seguidas. ')
            break
        else:
            print(f'Você ganhou! O resultado foi de {result}')
            vitoriasCons += 1
    if result % 2 != 0:
        if Jogador == 'impar':
            print(f'Você ganhou! O resultado foi de {result} ')
            vitoriasCons += 1
        else:
            print(f'Você perdeu! O resultado foi de {result} e você ganhou {vitoriasCons} vezes seguidas. ')
            break