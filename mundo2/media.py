#Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
#e quantas mulheres têm menos de 20 anos.
mediaIdade = int(0)
HomemMaisVelho = ''
Mulher20 = 0

for c in range(0,4):
   
    nome = str(input(f'Escreva o nome da {c+1}º pessoa: '))
    idade = str(input(f'Escreva a idade da {c+1}º pessoa em números inteiros: '))
    sexo = str(input(f'Digite o sexo da {c+1}º pessoa. [M]/[F]'))
    if idade.isnumeric():
        idade = int(idade)
        mediaIdade += idade
    else:
        print('ERRO! Você precisa digitar a idade da pessoa em números inteiros. Inicie o programa novamente.')
        exit()
    if c == 0:
        idade0 = idade
    else:
        if sexo == 'M' and idade0 < idade:
            idade0 = idade
            HomemMaisVelho = nome
    if sexo == 'M' and idade < 20:
        Mulher20 += 1
print(f'A média de idade das 4 pessoas é {mediaIdade / 4}, o nome do homem mais velho é {HomemMaisVelho} e {Mulher20} mulher(es) tem menos de 20 anos!')