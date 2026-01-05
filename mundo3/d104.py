n = input('Digite um número inteiro: ')
def leiaInt(numero):
    if not numero.isnumeric():
        while not numero.isnumeric():
            print('Você digitou um número inválido.')
            numero = input('Digite um número inteiro: ')
    return numero 
num_verificado = leiaInt(n)
num_verificado = int(num_verificado)
print(f'Você digitou o número {num_verificado}! ')