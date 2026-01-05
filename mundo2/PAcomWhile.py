termo1 = str(input('Digite o primeiro termo da progressãao aritmética em números inteiros: '))
if termo1.isnumeric():
    termo1 = int(termo1)
else:
    while not termo1.isnumeric():
        print('Você digitou um valor inválido!')
        termo1 = str(input('Digite o valor novamente apenas usando números inteiros: '))
    termo1 = int(termo1)

razao = str(input('Digite a razão da progressão aritmética em números inteiros: '))
if razao.isnumeric():
    razao = int(razao)
else:
    while not razao.isnumeric():
        print('Você digitou a razão usando valores inválidos!')
        razao = str(input('Digite a razão novamente apenas usando números inteiros: '))
    razao = int(razao)
    
contador = 0
termo_atual = termo1
while contador < 10:
    print(termo_atual)
    termo_atual += razao
    contador += 1
    if contador == 10:
        maisTermos = str(input('Você quer adicionar quantos outros termos? Responda usando números inteiros:'))
        if maisTermos.isnumeric():
            maisTermos = int(maisTermos)
        else:
            print('Você digitou um valor inválido!')
            maisTermos = str(input('Digite o valor novamente usando apenas números inteiros: '))
        maisTermos = int(maisTermos)

        if maisTermos > 0:
            contador -= maisTermos
