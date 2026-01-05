salario = float(input('Qual é o seu salário? '))
if salario > 1250 :
    salario = salario * 1.10
else:
    salario = salario * 1.15
print(f'Você recebeu um aumento! Seu novo salário será de {salario}')