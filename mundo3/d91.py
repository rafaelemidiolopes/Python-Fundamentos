import random
jogadores = {}
contador = 0
jogadores['jogador1'] = random.randint(1,6)
jogadores['jogador2'] = random.randint(1,6)
jogadores['jogador3'] = random.randint(1,6)
jogadores['jogador4'] = random.randint(1,6)
for i, v in enumerate(jogadores):
    print(f'o jogador {i+1} tirou {jogadores[v]}')
jogadoresEmordem = dict(sorted(jogadores.items(), key=lambda item: item[1], reverse=True))
print(f'=-'*30)
for i, v in enumerate(jogadoresEmordem):
    print(f'{i+1}º lugar: {v} com {jogadoresEmordem[v]} pontos ')
