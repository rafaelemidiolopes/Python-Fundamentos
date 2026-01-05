genero = str(input('Qual é o seu gênero? [M] / [F]   ')).upper()
while genero != 'M' and genero != 'F':
    genero = str(input('Gênero inválido. Digite seu gênero corretamente! [M] / [F]   ')).upper()
print('Seu gênero é feminino ' if genero == 'F' else 'Seu gênero é masculino')