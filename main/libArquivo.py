from rich import print
from interface import *
from rich.console import Console

Console = Console()
arq_animais = 'animais.txt'
arq_adotante = 'adotante.txt'

def arquivoExiste(nome):
    try:
        a = open(nome,'rt')
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
    except:
        print('[red]Houve um ERRO ao criar o arquivo![[/]]')
    else:
        print(f'[green]Arquivo {nome} criado com sucesso![/] ')

def lerArquivo_adotante(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('[red]Erro ao ler o arquivo[/]')
    else:
        cabeçalho('Adotantes cadastrados')
        c = 1
        for linha in a:
            dado = linha.split(';')
            print(f'1. {dado[0]} - {dado[1]} - {dado[2]} - {dado[3]} - {dado[4]} - {dado[5]} - {dado[6]}')
            c += 1
    finally:
        a.close()

def cadastrar_adotante(arq, nome = 'desconhecido', idade = 0, cpf=0, data_nascimento=0, endereço='Não definido', cidade='Não definido', estado='Não definido'):
    try:
        a = open(arq, 'at')
    except:
        print('[red]Houve um ERRO na abertura do arquivo[[/]]')
    else:
        try:
            a.write(f'{nome};{idade} anos;{cpf};{data_nascimento};{endereço};{cidade};{estado}')
        except:
            print('[red]Houve um ERRO ao escrever os dados![[/]]')
        else:
            print(f'[green]Novo registro de {nome} adicionado.[/]')
            a.close()

def adicionar_animal(arq_animais = "animais.txt", nome_animal = "deconhecido", especie_animal = "desconhecida", raca_animal = "raça não informada",
    cor_animal = "cor não informada", porte_animal = "Porte não informado", idade_animal = "0", observacao_animal = "Não ha observações."  ):
    nome_animal = Console.input("[green]1.[/] Digite o nome do animal: ")
    especie_animal = Console.input("[green]2.[/] Digite a espécie do animal que será adicionado: ")
    raca_animal = Console.input("[green]3.[/] Digite a raça do animal: ")
    cor_animal = Console.input("[green]4.[/] Digite a cor do animal: ")
    porte_animal = Console.input("[green]5.[/] Informe se o porte do animal é Pequeno, Médio ou Grande: ")
    idade_animal = Console.input("[green]6.[/] Informe a idade do animal: ")
    observacao_animal = Console.input("[green]7.[/] se necessário adicione alguma observação ao animal adicionado: ")
    try:
        a = open(arq_animais, 'at')
    except:
        print("Houve um erro ao adicionar os dados do animal!")
    else:
        try:
            a.write(f'{nome_animal};{especie_animal};{raca_animal};{cor_animal};{porte_animal};{idade_animal};{observacao_animal};\n')
        except:
            print("Houve um erro ao escrever os dados!")
        else:
            print(f"Novo registro de [blue]{nome_animal}[/] adicionado.")

def lista_animais(arq_animais='animais.txt'):
    try:
        a = open(arq_animais, 'rt')
    except:
        Console.print(f'[red]Erro ao abrir o arquivo![/]')
    else:
        cabeçalho("animais cadastrados")
        contador = 1
        for i in a:       
            dado = i.split(';')
            dado[1] = dado[1].replace('\n',';')
            Console.print(f'{contador}. {dado[0]} - {dado[1]} - {dado[2]} - {dado[3]} - {dado[4]} - {dado[5]} - {dado[6]} {dado[7]}')
            contador +=1

def opc3():
    cabeçalho('NOVO CADASTRADO')
    nome_adotante = Console.input('[green]1.[/] Nome: ')
    idade = Console.input('[green]2.[/] idade: ')
    cpf = Console.input('[green]3.[/] CPF[xxx.xxx.xxx-xx]: ')
    nascimento = Console.input('[green]4.[/] Data de nascimento[xx/xx/xxxx]: ')
    endereço = Console.input('[green]5.[/] Endereço: ')
    cidade = Console.input('[green]6.[/] Cidade: ')
    estado = Console.input('[green]7.[/] Estado: ')
    cadastrar_adotante(arq_adotante,nome_adotante,idade,cpf,nascimento,endereço,cidade,estado)