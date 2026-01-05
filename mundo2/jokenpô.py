import random
Player = str(input('Escolha entre pedra, papel e tesoura: ').capitalize())
Pc = str(random.choice(['Pedra', 'Papel', 'Tesoura']))


if Pc == Player:
    print('Não tivemos nenhum vencedor, deu empate!')
elif Player not in ['Pedra', 'Papel', 'Tesoura']:
    print('Escolha invalida, digite novamente! ')
    Player = str(input('Escolha entre pedra, papel e tesoura: ').capitalize())

elif Pc == 'Pedra' and Player == 'Tesoura' or Pc == 'Papel' and Player == 'Pedra' or Pc == 'Tesoura' and Player == 'Papel':
    print(f'Você perdeu! Tente novamente.')
else: print(f'Você ganhou! Você escolheu {Player} e a máquina escolheu {Pc}')