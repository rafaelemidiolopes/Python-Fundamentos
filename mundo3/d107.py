import moeda 
valor = int(input('Digite um valor: '))
print(f'Aumentando 13%, temos:', (moeda.aumentar(valor, 13, False)))

valor = int(input('Digite um valor: '))
print(f'Diminuindo 13%, temos:', (moeda.diminuir(valor, 13, False)))

valor = int(input('Digite um valor: '))
print(f'O dobro de {valor} é:', (moeda.dobro(valor, True)))

valor = int(input('Digite um valor: '))
print(f'A metade de {valor} é:', (moeda.metade(valor, True)))