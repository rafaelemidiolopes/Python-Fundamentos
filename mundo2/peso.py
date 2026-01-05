PesoPessoa = ''
for c in range(0,5):
    PesoPessoa = input(f'Digite o peso de {c+1}º pessoa em números inteiros: ')
    if PesoPessoa.isnumeric():
        PesoPessoa = int(PesoPessoa)
        if c == 0:
            maior = PesoPessoa
            menor = PesoPessoa
        else:
            if PesoPessoa < menor:
                menor = PesoPessoa
            elif PesoPessoa > maior:
                maior = PesoPessoa
    else:
        print('ERRO. Você precisa digitar o peso em números inteiros. Reinicie o programa! ')
        exit()
print(f'O maior peso digitado foi {maior}, e o menor foi {menor}!')