import json

def CriarAddArq(listaPessoas):
    try:
        with open("cadastro.json", "w", encoding="UTF-8") as arq:
            json.dump(listaPessoas, arq, indent=1, ensure_ascii=False)
    except:
        print('Erro ao adicionar pessoas. Tente novamente')

def lerArquivo():
    try:
        with open("cadastro.json", 'r+', encoding='utf-8') as arq:
            dados = json.load(arq)
            return dados
    except json.decoder.JSONDecodeError:
        print('Erro. Nenhuma pessoa foi cadastrada até o momento')
    except: 
        print('Ocorreu um erro na leitura do arquivo, feche o programa e tente novamente! ')

print('=' * 30)
print('          MENU PRINCIPAL        ')
print('=' * 30)
pessoas = lerArquivo()
escolha = 0


while escolha != 3:
    print('      MENU PRINCIPAL        ')
    print('1- Ver pessoas cadastradas')
    print('2- Cadastrar nova pessoa ')
    print('3- Sair do programa')
    print('=' * 30)
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
                CriarAddArq(pessoas)
                break
        print('=' * 30)
    if escolha == 1:
        print('=' * 30)
        print('       Pessoas cadastradas      ')
        print('=' * 30)
        for i, v in enumerate(pessoas):
            print(f'{v["nome"]}           {v["idade"]}')
        print('='* 30)
if escolha == 3:
    print('Saindo do programa... ')