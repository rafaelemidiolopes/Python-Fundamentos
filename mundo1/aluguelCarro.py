#Este script tem o propósito de calcular o custo total do aluguel do carro
dias = int(input('Por quantos dias vc alugou o carro? '))
kmRod = float(input('Quantos km aproximadamnte vc rodou? '))
PagDia = 60 * dias
PagKm = 0.15 * kmRod
PagTotal = PagDia + PagKm
print(f'O total a ser pago é de R${PagTotal:.2f} reais')