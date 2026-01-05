valor = float(input('Qual é o valor do produto que você deseja pagar? '))
formaPag = str(input('E qual seria a forma de pagamento? [Dinheiro] [Cheque] [Cartão] '))

if formaPag == 'Dinheiro' or formaPag == 'Cheque':
    print(f'Você ganhará 10% de desconto, tendo que pagar {valor * 0.90}')
elif formaPag == 'Cartão':
    formaCartao = input('Você deseja parcelar ou pagar a vista? [À vista] [Parcelado] ')
    formaCartao = formaCartao.lower()
    if formaCartao == 'parcelado':
        vezesCartao = int(input('Você deseja parcelar em quantas vezes?[1] [2] [3]...? '))
        if vezesCartao <=2:
            print(f'Você pagará R${valor}')
        else:
            print(f'Você ganhará um juros de 20%, tendo que pagar R${valor + (valor * 0.20)}')      
    elif 'vista' in formaCartao:
        print(f'Você ganhou um desconto de 5%, terá que pagar R${valor * 0.95}')