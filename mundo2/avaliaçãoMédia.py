nota1 = float(input('Qual foi sua primeira nota? '))
nota2 = float(input('Qual foi sua segunda nota? '))
média = (nota1 + nota2) / 2

if média < 5:
    print(f'Sua média foi de {média:.1f} e foi reprovado!')
elif média >= 5 and média < 7:
    print(f'Sua média foi de {média:.1f} e você ficou de recuperação!')
else:
    print(f'Sua média foi de {média:.1f} e você foi aprovado!')