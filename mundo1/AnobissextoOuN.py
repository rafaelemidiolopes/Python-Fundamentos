import calendar
ano = int(input('Digite um ano: '))
BissextoOuNao = calendar.isleap(ano)
if BissextoOuNao == False: 
    print(f'{ano} não é bissexto!')
else:
    print(f'{ano} é bissexto!')