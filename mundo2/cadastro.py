idade = None
sexo = None
varControle = None
PessoasMais18 = 0
homens = 0
mulherMenos20 = 0
while True:
    sexo = str(input('Digite o sexo de uma pessoa. [M]/[F]').strip().lower())
    if sexo != 'm' and sexo != 'f':
        while sexo != 'm' and sexo != 'f':
            sexo = str(input('Você digitou uma entrada inválida! Por favor, digite "M" para escolher o sexo masculino ou "F" para escolher o sexo feminino: ').strip().lower())
    idade = str(input('Digite a idade da pessoa usando apenas números inteiros: ').strip())
    if idade.isnumeric():
        idade = int(idade)
    else:
        while not idade.isnumeric():
            idade = str(input('Você digitou um valor inválido! Por favor, digite a idade novamente usando apenas números inteiros: ').strip())
        idade = int(idade)
    if idade > 18:
        PessoasMais18 += 1
    if sexo == 'm':
        homens += 1
    if sexo == 'f' and idade < 20:
        mulherMenos20 += 1
    varControle = str(input('Você deseja continuar o programa? [S]/[N]').strip().lower())
    if varControle != 's' and varControle != 'n':
        while varControle != 's' and varControle != 'n':
            varControle = str(input('Você digitou uma entrada inválida! Por favor, digite "S" para continuar o programa ou "N" para encerrar o programa: ').lower().strip())
    if varControle == 'n':
        break
print(f'No total, {PessoasMais18} pessoas tem mais de 18 anos, {homens} são do sexo masculino e {mulherMenos20} são do sexo feminino e tem menos de 20 anos! ')