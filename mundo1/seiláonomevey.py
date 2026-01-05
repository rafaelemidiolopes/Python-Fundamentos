#este script tem o objetivo de manipular strings
nome = input('Digite seu nome completo: ')
print('Seu nome em letras maiúsculas ',nome.upper())
print('Seu nome em letras minúsculas', nome.lower())
nomeDividido = nome.split()
print('Seu primeiro nome contém ', len(nomeDividido[0]), ' letras')
nomeReplace = nome.replace(' ', '')
print('Seu nome contém ',len(nomeReplace), ' letras')