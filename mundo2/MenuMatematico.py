continuar = True
while continuar:
    valor1 = str(input('Digite um valor em números inteiros: '))
    valor2 = str(input('Digite outro valor em números inteiros: '))
    if valor1.isnumeric() and valor2.isnumeric():
        valor1 = int(valor1)
        valor2 = int(valor2)
    else:
        while not valor1.isnumeric() or not valor2.isnumeric():
            print('Você inseriu um valor inválido. Insira todos os valores em números inteiros!')
            valor1 = str(input('Digite o primeiro valor em números inteiros: '))
            valor2 = str(input('Digite o segundo valor em números inteiros: '))
    valor1 = int(valor1)
    valor2 = int(valor2)
    print('='* 40)
    print(' '* 10, 'Menu Matemático')
    print('='* 40)
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos valores')
    print('[5] Sair do programa')
    valorMenu = str(input('Este é o nosso menu matemático. Digite o que você deseja fazer seguindo o valor inteiro de acordo com o menu matemático! '))
    if valorMenu.isnumeric():
        valorMenu = int(valorMenu)
        while valorMenu <= 0 or valorMenu >= 6:
            valorMenu = str(input('Valor inválido! Digite apenas um valor entre 1 e 5: '))
            if valorMenu.isnumeric():
                valorMenu = int(valorMenu)
            else:
                while not valorMenu.isnumeric():
                    valorMenu = str(input('Valor inválido! Digite apenas um valor entre 1 e 5: '))
                valorMenu = int(valorMenu)
    else:
        while not valorMenu.isnumeric():
            print('Você digitou um valor inválido. Escolha um dos 5 números do menu e digite para fazer a operação designada! ')
            valorMenu = str(input('Novo valor: '))
    valorMenu = int(valorMenu)
    if valorMenu == 1:
        soma = valor1 + valor2
        print(f'A soma entre {valor1} e {valor2} é {soma}!')
    elif valorMenu == 2:
        multiplicação = valor1 * valor2
        print(f'A multiplicação entre {valor1} e {valor2} é de {multiplicação}!')
    elif valorMenu == 3:
        maior = valor1
        if valor2 > valor1:
            maior = valor2
        print(f'O maior valor entre {valor1} e {valor2} é {maior}!')
    elif valorMenu == 4:
        print('Ok. Vamos pegar novos valores! ')#aqui preciso criar novas variaveis pra essess valores? como faço isso? e se o usuario quiser novos valores 1000 vezes?
    elif valorMenu == 5:
        print('Saindo...')
        continuar = False
        exit()