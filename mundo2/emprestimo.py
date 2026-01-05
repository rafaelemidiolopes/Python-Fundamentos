valorCasa = float(input('Qual é o valor da casa que você quer financiar? '))
salario = float(input('Qual é o seu salário? '))
anosParaPagar = int(input('Em quantos anos você irá pagar a casa? '))

parcelasTotais = 12 * anosParaPagar
valorTotalDeTodasParcelas = valorCasa / parcelasTotais

if valorTotalDeTodasParcelas > (salario * 0.3): 
    print(f'Infelizmente seu empréstimo foi negado! Pois o valor de cada parcela ultrapassa 30% do seu salário. Você iria precisar nos pagar R${valorTotalDeTodasParcelas:.2f} divididos em {parcelasTotais} parcelas.')
else: 
    print(f'Meus parabéns. Seu empréstimo foi aprovado! Você precisa pagar R${valorTotalDeTodasParcelas:.2f} divididos em {parcelasTotais} parcelas!')