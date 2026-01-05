import random
import time
QuantJogos = int(input('Quantos jogos você quer que eu sorteie? '))
jogo = []
lista = []
tot = 1
while tot <= QuantJogos:
    cont = 0
    tot += 1
    while True:
        num = random.randint(1, 60) 
        if num not in lista:
            lista.append(num)
            cont += 1 
        if cont == 6:   
            break
    lista.sort()
    jogo.append(lista[:])
    lista.clear()
for i, v in enumerate(jogo):
    print(f'Jogo {i+1}: {v}')
    time.sleep(1)
print('Boa Sorte!')