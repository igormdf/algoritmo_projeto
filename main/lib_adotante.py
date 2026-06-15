from rich import print
from interface import *
from rich.console import Console
from rich.panel import Panel

Console = Console()
arq_adotante = 'adotante.txt'

def lerArquivo_adotante(nome):
    try:
        arquivo = open(nome, 'rt')
    except:
        print('[red]Erro ao ler o arquivo[/]')
    else:
        cabeçalho2("Adotantes cadastrados")
        c = 1
        for linha in arquivo:
            dado = linha.split(';')
            print(f'{c}. [bold blue]Nome:[/] {dado[0]} | [bold blue]Idade:[/] {dado[1]} | [bold blue]CPF:[/] {dado[2]} | [bold blue]Nascimento:[/] {dado[3]} | [bold blue]Endereço:[/] {dado[4]} | [bold blue]Cidade:[/] {dado[5]} | [bold blue]Estado:[/] {dado[6]}')
            c += 1
        if c == 1:
            Console.print(f'[yellow]Ainda não foram adicionados adotantes a lista![/]')
    finally:
        arquivo.close()

def auxílio_addAdotante(arq_adotante, nome, idade, cpf, data_nascimento, endereço, cidade, estado):
    try:
        arquivo = open(arq_adotante, 'at')
    except:
        print('[red]Houve um ERRO na abertura do arquivo[[/]]')
    else:
        if (nome == '' or idade == '' or cpf == '' or
            data_nascimento == '' or endereço == '' or
            cidade == '' or estado == '' or len(cpf) != 11 or len(data_nascimento) != 8):
            Console.print('[red]ERRO!!Todos os dados não foram preenchidos com sucesso.[/]')
            Console.print('[red]Prencha os dados novamente de maneira correta.[/]')
            adicionar_adotante()
        else:
            try:
                arquivo.write(f'{nome};{idade} anos;{cpf};{data_nascimento};{endereço};{cidade};{estado}\n')
            except:
                print('[red]Houve um ERRO ao escrever os dados![[/]]')
            else:
                print(f'[green]Novo registro de {nome} adicionado.[/]')
                arquivo.close()
            finally:
                arquivo.close()

def adicionar_adotante():
    cabeçalho2('NOVO CADASTRO')
    nome_adotante = Console.input('[green]1.[/] Nome: ')
    idade = Console.input('[green]2.[/] idade: ')
    cpf = Console.input('[green]3.[/] CPF[11 dígitos]: ')
    nascimento = Console.input('[green]4.[/] Data de nascimento [DD/MM/YYYY]: ')
    endereço = Console.input('[green]5.[/] Endereço: ')
    cidade = Console.input('[green]6.[/] Cidade: ')
    estado = Console.input('[green]7.[/] Estado: ')
    auxílio_addAdotante(arq_adotante,nome_adotante,idade,cpf,nascimento,endereço,cidade,estado)

def remover_adotante():
    try:
        arquivo = open(arq_adotante, 'r')
    except:
        print('[red]Houve um ERRO na abertura do arquivo[[/]]')
    else:
        linhas = arquivo.readlines()
        if len(linhas) == 0:
            return f'[yellow]Ainda não foram adicionados adotantes a lista![/]'
        while True:
            try:
                quem_remover = leiaint('Escolha o número de quem remover: ')
            except:
                print('[red]Digite um valor válido![/]')
            #except ValueError:
               #print('[red]Digite um valor válido![/]')
            else:
                break
        linha_remover = quem_remover - 1
        while True:
            if linha_remover < len(linhas):
                del linhas [linha_remover]
                break
            else:
                print('[red]Esse número não é válido!!![/]')
                while True:
                    try:
                        quem_remover = leiaint('Escolha o número de quem remover: ')
                    except:
                        print('[red]Digite um valor válido![/]')
                    else:
                        break
                linha_remover = quem_remover - 1
        try:
            arquivo = open(arq_adotante, 'w')
        except:
            print('[red]Houve um ERRO na abertura do arquivo[[/]]')
        else:
            try:
                arquivo.writelines(linhas)
            except:
                print('[red]Houve um ERRO ao remover os dados![[/]]')
            else:
                print(f'[green]Adotante[/] correspondente ao número {quem_remover} [red]removido com sucesso[/]')
            finally:
                arquivo.close()