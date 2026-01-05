jogadores = []
gols = []
contador = 0
while True:
    dados = {'nome_jogador': input('Qual é o nome do jogador? ').strip()}
    dados['partidas'] = int(input(f'Quantas partidas {dados["nome_jogador"]} jogou? '))
    dados['total_gols'] = 0
    for c in range(1, dados['partidas']+1):
        gols.append(int(input(f'Quantos gols {dados["nome_jogador"]} marcou na partida {c}? ')))
        dados['total_gols'] += gols[-1]
    dados['gols_marcados'] = gols.copy()
    jogadores.append(dados)
    continuar = input('Você deseja continuar? [S]/[N]').strip().upper()[0]
    if continuar == 'N':
        break
print('-=' * 40)
print('Cod     nome          gols          total')
print('-'* 40)
for i, v in enumerate(jogadores):
    print(f'{i}     {v["nome_jogador"]}      {v["gols_marcados"]}    {v["total_gols"]}')
while True:
    dados_jogador = int(input('Mostrar dados de qual jogador? Use o codigo dele na lista ou digite 999 para encerrar o programa: '))
    if dados_jogador == 999:
        print('Encerrando...')
        break
    novarvar = jogadores[dados_jogador-1]
    print(f'Levantamento do jogador {novarvar["nome_jogador"]}')
    for c in range (novarvar["partidas"]):
        contador += 1
        print(f'No jogo {contador} fez {novarvar["gols_marcados"][c]}')
          
         