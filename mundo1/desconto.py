# Este script tem o propósito de calcular o preço com desconto de 5%
preço = float(input('qual o valor da coisa q vc quer comprar? '))
desc = 5 / preço * 100
print(f'com 5% de desconto ficaria {preço - desc:.2f} ')