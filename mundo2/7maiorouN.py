maioridade = 0
dataNasc = ''
for c in range(0,7):
    dataNasc = input('Digite o ano de nascimento da {c+1}º pessoa:')
    if dataNasc.isnumeric():
        dataNasc = int(dataNasc)
    else:
        print('ERRO! Você precisa digitar apenas números inteiros. Reinicie o programa.')
        exit()
    if 2025 - dataNasc >= 18:
        maioridade += 1
print(f'Dessas 7 pessoas, {maioridade} estão na maioridade!')