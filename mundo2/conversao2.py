num = int(input('Digite um número inteiro: '))
escolha = int(input('Digite 1 para converter esse valor para binário, digite 2 para converter esse valor para octal ou digite 3 para converter esse valor para hexadecimal: '))
if escolha == 1:
    num = bin(num)
    print(f'O valor convertido é {num[:2]}')
elif escolha == 2:
    num = oct(num)
    print(f'O valor convertido é {num[:2]}')
elif escolha == 3:
    num = hex(num)
    print(f'O valor convertido é {num[:2]}') 