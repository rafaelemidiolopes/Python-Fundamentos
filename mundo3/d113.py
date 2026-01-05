def leiaInt(msg1, msg2):
    while True:
        try: 
            nInt = int(input(msg1))
        except(ValueError, TypeError):
            print('ERRO! Digite um número inteiro válido! ')
            continue 
        else:
            break
    while True:
        try: 
            nReal = float(input(msg2))
        except(ValueError, TypeError):
            print('ERRO! Digite um valor real válido! ') 
            continue
        else:
            return nInt, nReal
num = leiaInt('Digite um número inteiro: ', 'Digite um valor real: ')
print(f'O número inteiro digitado foi {num[0]}, o número real digitado foi {num[1]}! ')