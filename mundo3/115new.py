import json
def salvar(pessoas):
    with open("cadastro.json", "w", encoding="utf-8") as arq:
        json.dump(pessoas, arq, indent=1, ensure_ascii=False)
def carregar():
    try:
        with open("cadastro.json", "r") as arq:
            return json.load(arq)
    except FileNotFoundError:
            return []

print('='* 30)
print('      MENU PRINCIPAL      ')
print('='* 30)

pessoas = carregar()
escolha = 0


while escolha != 3:
    print('    MENU PRINCIPAL     ')
    print('1- Ver pessoas cadastradas')
    print('2- Cadastrar nova pessoa ')
    print('3- Sair do programa')
    print('='* 30)
    
    while True:
        try:
            escolha = int(input('Sua opção: '))
        except:
            print('ERRO! Digite uma opção válida')
            continue
        else:
            if escolha > 3 or 0 > escolha:
                print('ERRO! Digite uma opção entre 1 e 3 ')
                continue
            else:
                break
    
    if escolha == 2:
        while True:
            pessoa = {}
            try:
                pessoa['nome'] = input('Qual é o nome da pessoa a ser cadastrada? ').strip().capitalize()
            except ValueError:
                print('ERRO! Digite um nome válido usando apenas letras')
                continue
            try:
                pessoa['idade'] = int(input('Digite a idade da pessoa a ser cadastrada usando apenas números inteiros: '))
            except ValueError:
                print('VALOR INVÁLIDO! Digite a idade usando apenas números inteiros')
                continue
            else:
                pessoas.append(pessoa)
                salvar(pessoas)
                break
        print('='* 30)
    
    if escolha == 1:
        if len(pessoas) == 0:
            print('Nenhuma pessoa foi cadastrada até o momento! ')
            print('='* 30)
        else:
            print('='* 30)
            print('      Pessoas cadastradas    ')
            print('='* 30)
            for i, v in enumerate(pessoas):
                print(f'{v["nome"]}                       {v["idade"]}')
            print('='* 30)

if escolha == 3:
    print('Saindo do programa... ')