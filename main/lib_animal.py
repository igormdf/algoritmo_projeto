from rich.console import Console
from rich import print
from interface import *

Console = Console()
arq_animais = 'animais.txt'

def adicionar_animal(arq_animais = "animais.txt", nome_animal = "deconhecido", especie_animal = "desconhecida", raca_animal = "raça não informada",
    cor_animal = "cor não informada", porte_animal = "Porte não informado", idade_animal = "0", observacao_animal = "Não ha observações."  ):
    a = open(arq_animais, 'r')
    linha = a.readlines()
    total_linhas = len(linha) + 1
    try:
        a = open(arq_animais, 'at')
    except:
        print("Houve um erro ao adicionar os dados do animal!")
    else:
        try:
            a.write(f'{total_linhas}. {nome_animal};{especie_animal};{raca_animal};{cor_animal};{porte_animal};{idade_animal};{observacao_animal};\n')
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
        if contador == 1:
            Console.print(f"[yellow]Ainda não foram adicionados animais a lista![/]")

def opção_1():
    nome_animal = Console.input("[green]1.[/] Digite o nome do animal: ")
    especie_animal = Console.input("[green]2.[/] Digite a espécie do animal que será adicionado: ")
    raca_animal = Console.input("[green]3.[/] Digite a raça do animal: ")
    cor_animal = Console.input("[green]4.[/] Digite a cor do animal: ")
    porte_animal = Console.input("[green]5.[/] Informe se o porte do animal é Pequeno, Médio ou Grande: ")
    idade_animal = Console.input("[green]6.[/] Informe a idade do animal: ")
    observacao_animal = Console.input("[green]7.[/] se necessário adicione alguma observação ao animal adicionado: ")
    adicionar_animal(nome_animal,especie_animal,raca_animal,cor_animal,porte_animal,idade_animal,observacao_animal)