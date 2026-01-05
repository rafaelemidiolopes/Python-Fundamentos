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


def moeda(valor):
    return f'R${valor:.2f}'.replace('.', ',')