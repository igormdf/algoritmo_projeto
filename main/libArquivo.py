from rich import print
from interface import *

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
        for linha in a:
            dado = linha.split(';')
            print(f'{dado[0]} - {dado[1]} - {dado[2]} - {dado[3]} - {dado[4]} - {dado[5]} - {dado[6]}')
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