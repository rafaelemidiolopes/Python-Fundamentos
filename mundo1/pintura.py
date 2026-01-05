# Este script tem o propósito de calcular quantos litros de tinta será necessário para pintar uma parede
altura = float(input('qual a altura da parede? '))
largura = float(input('qual a largura da parede? '))
areaEmM2 = altura * largura
tintaLitroM2 = areaEmM2/ 2
print(f'a área da parede em metros quadrados é de {areaEmM2}m², irá gastar um total de {tintaLitroM2} litros de tinta')
