print('SISTEMA DE AJUDA')
def ajuda(resp):
    help(resp)


resp = input('Função ou biblioteca> ').strip().lower()
while resp != 'fim':
    ajuda(resp)
    resp = input('Função ou biblioteca> ').strip().lower()
print('=-'*10)
print('PROGRAMA FINALIZADO')
print('=-'*10) 