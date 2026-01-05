times = (
    'Flamengo', 'Cruzeiro', 'Bragantino', 'Palmeiras', 'Bahia', 'Fluminense', 'Atlético-MG', 'Botafogo','Mirassol', 'Corinthians', 'Grêmio', 'Ceará SC', 'Vasco da Gama', 'São Paulo', 'Santos', 'EC Vitória', 'Internacional', 'Fortaleza', 'Juventude', 'Sport Recife')
os5primeiros = times[0:5]
ultimos4 = times[16:20]
timesOrdemAlfabetica = sorted(times)
posicaoCorinthians = times.index('Corinthians')
print(f'Os primeiros 5 colocadoss são: {os5primeiros}, os 4 útimos colocados são {ultimos4}, os times em ordem alfabetica é {timesOrdemAlfabetica} e o Corinthians está na posição {posicaoCorinthians+1}º!')