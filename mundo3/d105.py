def notas(*notas, sit = False):
    menor = notas[0]
    maior = notas[0]
    boletim = {'total': 0, 'maior': maior, 'menor': menor, 'média': 0}
    boletim['total'] = len(notas)
    for k, v in enumerate(notas):
        if v > maior:
            maior = v 
        if v < menor:
            menor = v
    boletim['maior'] = maior
    boletim['menor'] = menor
    media = sum(notas) / len(notas)
    boletim['média'] = media
    if sit == True:
        if media < 5:
            boletim['situação'] = 'Ruim'
        elif media >= 5 and media <= 7:
            boletim['situação'] = 'Razoável'
        else:
            boletim['situação'] = 'Boa'
         
    return boletim
resp = notas(1, 2, 3.5, sit=True)
print(resp) 