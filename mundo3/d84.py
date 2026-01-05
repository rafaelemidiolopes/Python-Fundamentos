pessoas = []
PessoasPesadas = []
PessoasLeves = []
contador = 0
while True:
    contador +=1
    pessoas.append(str(input('Digite o nome da pessoa a ser cadastrada: ')))
    pessoas.append(int(input('Digite o peso dessa pessoa usando apenas números inteiros: '))) 
    if contador == 1:
        PessoasLeves.append(pessoas[0]) 
        PessoasPesadas.append(pessoas[0]) 
    if pessoas[-1] > PessoasPesadas[0:0]: 
        PessoasPesadas.remove([-1]) 
        PessoasPesadas.append(pessoas[:])
    if pessoas[-1] < PessoasLeves[0:0]:
        PessoasLeves.remove([-1])
        PessoasLeves.append(pessoas[-1])
    varControle = input('Você deseja continuar adicionando pessoas? [S]/[N]').strip().upper()[0]
    if varControle == 'N':
        break
print(f'Você digitou {len(pessoas)} pessoas, as mais pesadas são {PessoasPesadas} e as mais leves são {PessoasLeves}')