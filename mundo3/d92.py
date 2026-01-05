dados = {'Nome': input('Qual é o seu nome? ').strip(), 'anoNasc': int(input('Digite o seu ano de nascimento: ')), 'cpts': int(input('Você possui carteira de trabalho? Caso não tenha digite 0: '))}
idade = 2025 - dados['anoNasc']
if dados["cpts"] != 0:
    dados['anoContratado'] = int(input('Em qual ano você foi contratado? '))
    dados['salário'] = float(input('Qual é o seu salario? R$'))
    IdadeAposent = idade + (35 - (2025 - dados['anoContratado']))
    print('-=' * 40,f'\nSeu nome é {dados["Nome"]} \nSua idade é {idade} \nSeu CPTS tem o valor de {dados["cpts"]} \nVocê foi contratado(a) no ano de {dados["anoContratado"]} \nSeu salário é de {dados["salário"]} \nVocê poderá se aposentar com {IdadeAposent} anos! ')
else:
    print(f'Seu nome é {dados["Nome"]} \nSua idade é {idade} \nNão é possível calcular o ano de aposentadoria de quem não possui CPTS! ')

            
            
            
