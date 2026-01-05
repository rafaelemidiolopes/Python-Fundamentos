dados = {}
dados['nome'] = input('Digite o nome do aluno: ').strip()
dados['média'] = float(input('Digite a média do aluno: '))
if dados['média'] >= 5:
    dados['situação'] = 'Aprovado'
else:
    dados['situação'] = 'Reprovado'
for c in range (1):
    print(f'O nome do aluno é {dados["nome"]}')
    print(f'A média é igual a {dados["média"]}')
    print(f'A situação é {dados["situação"]}! ')