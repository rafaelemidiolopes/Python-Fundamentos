def aumentar(valor, n, mostrar = False):
    valor += (n / 100) * valor 
    return valor if mostrar == False else moeda(valor)


def diminuir(valor, n, mostrar = False):
    valor -= (n / 100) * valor 
    return valor if mostrar == False else moeda(valor)



def dobro(valor, mostrar = False):
    valor *=2
    return valor if mostrar == False else moeda(valor)


def metade(valor, mostrar = False):
    valor = valor / 2
    return valor if mostrar == False else moeda(valor)

def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).strip()
        if entrada.isalpha() or entrada.strip() == '':
            print('ERRO. Entrada inválida! ') 
        else:
            valido = True
            entrada = entrada.replace(',', '.') 
            return float(entrada)   
    
def moeda(valor):
    return f'R${valor:.2f}'.replace('.', ',')