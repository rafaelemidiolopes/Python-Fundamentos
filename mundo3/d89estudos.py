boletim = []
nome = ''
nota1 = 0
nota2 = 0
média = 0
while True:
    nome = input('Digite o nome do aluno: ')
    nota1 = float(input('Digite a primeira nota do aluno: '))
    nota2 = float(input('Digite a segunda nota do aluno: '))
    média = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], média])
    continuar = input('Você deseja continuar adicionando alunos? [S]/[N]').strip().upper()[0]
    if continuar == 'N':
        break
print('=-'*30)
print('Nº     Nome        Média')
print('-='*30)
for i, v in enumerate(boletim):
    print(f'{i+1}     {v[0]}      {v[2]}')
while True:
    verNotaAluno = int(input('Você deseja ver as notas de qual aluno? Digite o número dele que está na lista, ou 999 para encerrar o programa: '))
    if verNotaAluno == 999:
        print('Encerrando... ')
        break
    notasAluno = boletim[verNotaAluno-1]
    if verNotaAluno != 999:
        print(f'As notas de {notasAluno[0]} são {notasAluno[1]}! ')