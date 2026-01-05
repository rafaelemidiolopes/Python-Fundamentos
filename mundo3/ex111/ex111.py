import moeda.funcoes
valor = moeda.funcoes.leiaDinheiro('Digite um valor: ')
print(f'Aumentando 13%, temos:', (moeda.funcoes.aumentar(valor, 13, False)))

valor = moeda.funcoes.leiaDinheiro('Digite um valor: ')
print(f'Diminuindo 13%, temos:', (moeda.funcoes.diminuir(valor, 13, False)))

valor = moeda.funcoes.leiaDinheiro('Digite um valor: ')
print(f'O dobro de {valor} é:', (moeda.funcoes.dobro(valor, True)))

valor = moeda.funcoes.leiaDinheiro('Digite um valor: ')
print(f'A metade de {valor} é:', (moeda.funcoes.metade(valor, True)))