palavras = ('Ler', 'Estudar', 'Musica', 'Programar', 'Trabalhar', 'Evoluir', 'Academia', 'Natureza', 'Sapato', 'Frutas', 'Banana', 'Comida', 'Dinheiro', 'Carro')

for c in palavras:
    print(f'\nNa palavra {c.upper()} nós temos as vogais: ', end = '')
    for letras in c:
        if letras.lower() in 'aeiou':
            print(letras, end = ' ')