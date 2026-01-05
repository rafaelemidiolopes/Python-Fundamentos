def maior(*numeros):
    contador = 1
    if len(numeros) == 0:
        print('-='*40)
        print('Analisando os valores passados...')
        print('Foram informado 0 valores ao todo.')
        print('Não possui valor maior por não conter valores! ')
    else:
        print('-='*40)
        print('Analisando os valores passados...')
        for num in numeros:
            print(num, end=' ')
            if contador == 1:
                maior = num
                contador +=1
            if num > maior:
                maior = num
        print(f'foram informados, sendo {len(numeros)} números ao todo')
        print(f'O maior valor informado foi {maior}')

    
    
    
#programa principal
maior(-9, -7, -5, -2)
maior(-1, 0, -9, -8)
maior(2, 5)
maior(0)
maior()
