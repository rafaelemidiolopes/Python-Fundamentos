pessoas = []
mulheres = []
contador = 0
média_idade = 0
acima_Media = []
while True:
    pessoa = {'nome': input('Qual é o seu nome? ').strip(), 'sexo': input('Qual é o seu sexo? [M]/[F]').strip().upper()[0], 'idade': int(input('Qual é a sua idade? ').strip())}
    pessoas.append(pessoa)
    if pessoa["sexo"] == 'F':
        mulheres.append(pessoa['nome'])
    média_idade += pessoa['idade']
    continuar = input('Você deseja continuar cadastrando pessoas? [S]/[N] ').strip().upper()[0]
    contador += 1
    if continuar == 'N':
        break
média_idade = média_idade / contador
for i, v in enumerate(pessoas):
    if v['idade'] > média_idade:
        acima_Media.append(v)
print('-=' * 40)
print(f'Ao todo, temos {contador} pessoas cadastradas! ')
print(f'A média de idade é {média_idade}')
print(f'As mulheres cadastradas são: {mulheres}')
print(f'Lista das pessoas que estão acima da média de idade: ')
for i, v in enumerate(acima_Media):
    print(v)