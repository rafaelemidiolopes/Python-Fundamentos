def voto(anoNasc):
    if 2025 - anoNasc < 16:
        return 'negado' 
    elif 2025 - anoNasc == 16 or 2025 - anoNasc == 17 or 2025 - anoNasc >= 70:
        return 'opcional'
    else:
        return 'obrigatório' 
vota_ou_nao = voto(int(input('Qual é o seu ano de nascimento? ')))
print(f'O seu voto é {vota_ou_nao}')