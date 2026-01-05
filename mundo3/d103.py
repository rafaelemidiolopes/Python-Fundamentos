def ficha(nome = 'Desconhecido', gols = 0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato! ')
nome = input('Qual é o nome do jogador? ')
gols = input('Quantos gols ele marcou no campeonato? ')
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gols = gols)
else:
    ficha(nome, gols)