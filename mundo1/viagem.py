kmDaViagem = int(input('Quantos Km você deseja viajar? '))
if kmDaViagem < 250:
    valor = kmDaViagem * 0.50
    print(f'Você pagará o valor de R${valor} reais!')
else:
    valor = kmDaViagem * 0.45
    print(f'Você pagará o valor de R${valor} reais!')
