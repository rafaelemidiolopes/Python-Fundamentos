pessoas = []
maior = menor = contador = 0
while True:
    nome = str(input('Digite o nome da pessoa a ser cadastrada: '))
    peso = float(input('Digite o peso da pessoa a ser cadastrada: '))
    pessoa = [nome, peso]
    pessoas.append(pessoa)
    contador +=1 
    if contador == 1:
        maior = peso
        menor = peso
    if menor > peso:
        menor = peso
    if maior < peso:
        maior = peso
    continuar = str(input('Você desejar continuar? [S]/[N]')).strip().upper()[0]
    if continuar == 'N':
            break
print(f'Foram cadastradas {contador} pessoas, a(s) mais pesada(s) são', end = ' ')
for p in pessoas:
    if p[1] == maior:
        print(p[0],'e', end=' ')
for p in pessoas:
    if p[1] == menor:
        print(p[0], 'são as mais leves') 