boletim = []
nota1 = 0
nota2 = 0
media = 0
nome = ''
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Digite a nota 1: '))
    nota2 = float(input('Digite a nota 2: '))
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])
    continuar = str(input('Você deseja continuar adicionando alunos e suas notas? [S]/[N] ').strip().upper()[0])
    if continuar == 'N':
        break
print('=-' * 30)
print('Nº  Nome         Média')
print('-' * 20)
for i, v in enumerate(boletim):
    print(f'{i+1} {v[0]}      {v[2]}')
while True:
    mostrarNotas = int(input('Você deseja ver as notas de quem? Digite em números inteiros(999 encerra oprograma): '))
    notasAluno = boletim[mostrarNotas-1]
    if mostrarNotas == 999:
        print('Programa finalizado! ')
        break
    if mostrarNotas != 999:
        print(notasAluno[1])
