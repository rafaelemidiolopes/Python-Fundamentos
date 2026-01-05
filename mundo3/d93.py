dados = {'nome_jogador': input('Qual é o nome do jogador? ').strip()}
dados['partidas'] = int(input(f'Quantas partidas {dados["nome_jogador"]} jogou? '))
gols = []
dados['total_gols'] = 0
for c in range(1, dados['partidas']+1):
    gols.append(int(input(f'Quantos gols {dados["nome_jogador"]} marcou na partida {c}? ')))
    dados['total_gols'] += gols[-1]
dados['gols_marcados'] = gols.copy()
print('-=' * 40)
print(dados)
print('=-' * 40)
print(f'O nome do jogador é {dados["nome_jogador"]} \nO campo gols é {dados["gols_marcados"]} \nE marcou um total de {dados["total_gols"]} gols! ')
print('-=' * 40)
print(f'O jogador {dados["nome_jogador"]} jogou {dados["partidas"]} partidas.')
contador = 0
for k, v in dados.items():
    contador += 1
    print(f'-> Na partida {contador}, marcou {gols[contador-1]} gols.')
print(f'E foi um total de {dados["total_gols"]} gols! ')