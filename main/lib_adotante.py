from rich import print
from interface import *
from rich.console import Console

Console = Console()
arq_adotante = 'adotante.txt'

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
            print(f'{dado[0]} - {dado[1]} - {dado[2]} - {dado[3]} - {dado[4]} - {dado[5]} - {dado[6]}')
            c += 1
        if c == 1:
            Console.print(f'[yellow]Ainda não foram adicionados adotantes a lista![/]')
    finally:
        a.close()

def cadastrar_adotante(arq_adotante, nome = 'desconhecido', idade = 0, cpf=0, data_nascimento=0, endereço='Não definido', cidade='Não definido', estado='Não definido'):
    a = open(arq_adotante, 'r')
    linha = a.readlines()
    total_linhas = str(len(linha) + 1)
    a.close()
    try:
        a = open(arq_adotante, 'at')
    except:
        print('[red]Houve um ERRO na abertura do arquivo[[/]]')
    else:
        try:
            a.write(f'{total_linhas}. {nome};{idade} anos;{cpf};{data_nascimento};{endereço};{cidade};{estado}\n')
        except:
            print('[red]Houve um ERRO ao escrever os dados![[/]]')
        else:
            print(f'[green]Novo registro de {nome} adicionado.[/]')
            a.close()

def opção_3():
    cabeçalho('NOVO CADASTRADO')
    nome_adotante = Console.input('[green]1.[/] Nome: ')
    idade = Console.input('[green]2.[/] idade: ')
    cpf = Console.input('[green]3.[/] CPF[xxx.xxx.xxx-xx]: ')
    nascimento = Console.input('[green]4.[/] Data de nascimento[xx/xx/xxxx]: ')
    endereço = Console.input('[green]5.[/] Endereço: ')
    cidade = Console.input('[green]6.[/] Cidade: ')
    estado = Console.input('[green]7.[/] Estado: ')
    cadastrar_adotante(arq_adotante,nome_adotante,idade,cpf,nascimento,endereço,cidade,estado)

def remover_adotante(n):
    try:
        a = open(arq_adotante, 'r')
    except:
        print('[red]Houve um ERRO ao ler o arquivo[/]')
    else:
        linhas = a.readlines()
        removida = [linha for linha in linhas if '{n}' not in linha]
        a.close()
        try:
            a = open(arq_adotante, 'at')
        except:
            print('[red]Houve um ERRO na abertura do arquivo[[/]]')
        else:
            a.writelines(removida)