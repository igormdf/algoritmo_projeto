from rich.console import Console
from rich import print
from interface import *

console = Console()
arq_animais = 'animais.txt'

def auxílio_addAnimal(arq_animais, nome_animal, especie_animal, raca_animal,
    cor_animal, porte_animal, idade_animal, observacao_animal = "Não ha observações."  ):
    try:
        arquivo = open(arq_animais, 'at')
    except:
        print("Houve um erro ao adicionar os dados do animal!")
    else:
        if (nome_animal == '' or especie_animal == '' or raca_animal == '' or
            cor_animal == '' or porte_animal == '' or idade_animal == ''):
            console.print('[red]ERRO!!Todos os dados não foram preenchidos.[/]')
            console.print('[red]Prencha os dados novamente de maneira correta.[/]')
            adicionar_animal()
        else:
            try:
                arquivo.write(f'{nome_animal};{especie_animal};{raca_animal};{cor_animal};{porte_animal};{idade_animal};{observacao_animal};\n')
            except:
                print("Houve um erro ao escrever os dados!")
            else:
                print(f"Novo registro de [blue]{nome_animal}[/] adicionado.")

def lista_animais(arq_animais='animais.txt'):
    
    try:
        arquivo = open(arq_animais, 'rt')
    except:
        console.print(f'[red]Erro ao abrir o arquivo![/]')
    else:
        cabeçalho2("Animais cadastrados")
        contador = 1
        for i in arquivo:       
            dado = i.split(';')
            dado[1] = dado[1].replace('\n',';')
            console.print(f'{contador}. [bold blue]Nome:[/] {dado[0]} | [bold blue]Espécie:[/] {dado[1]} | [bold blue]Raça:[/] {dado[2]} | [bold blue]Cor:[/] {dado[3]} | [bold blue]Porte:[/] {dado[4]} | [bold blue]Idade:[/] {dado[5]} anos | [bold blue]Observação:[/] {dado[6]}')
            contador +=1
        if contador == 1:
            console.print(f"[yellow]Ainda não foram adicionados animais a lista![/]")

def adicionar_animal():
    cabeçalho2('NOVO CADASTRO')
    nome_animal = console.input("[green]1.[/] Digite o nome do animal: ")
    especie_animal = console.input("[green]2.[/] Digite a espécie do animal que será adicionado: ")
    raca_animal = console.input("[green]3.[/] Digite a raça do animal: ")
    cor_animal = console.input("[green]4.[/] Digite a cor do animal: ")
    porte_animal = console.input("[green]5.[/] Informe se o porte do animal é Pequeno, Médio ou Grande: ")
    idade_animal = console.input("[green]6.[/] Informe a idade do animal: ")
    observacao_animal = console.input("[green]7.[/] Observação: ")
    auxílio_addAnimal(arq_animais,nome_animal,especie_animal,raca_animal,cor_animal,porte_animal,idade_animal,observacao_animal)

def remover_animal():
    try:
        arquivo = open(arq_animais, 'r')
    except:
        print(f'[red]Houve um erro ao tentar ler o arquivo')
    else:
        linhas = arquivo.readlines()
        if len(linhas) == 0:
            return f'[yellow]Ainda não foram adicionados adotantes a lista![/]'
        while True:
            try:
                quem_remover = int(input('Escolha o número de quem remover: '))
            except:
                print('[red]Digite um valor válido![/]')
            else:
                break
        animal_remover = quem_remover - 1
        while True:
            if animal_remover < len(linhas):
                del linhas[animal_remover]
                break
            else:
                console.print('[red]Esse número não é valido[/]')
                quem_remover = int(input("Escolha um numero válido para remover: "))
                animal_remover = quem_remover - 1
        try:
            arquivo = open(arq_animais, 'w')
        except:
            console.print(f'[red]Não foi possivel ler a lista![/]')
        else:
            try:
                arquivo.writelines(linhas)
            except:
                console.print(f'[red] Houve um erro ao remover os dados')
            else:
                console.print(f'[green]Animal[/] correspondente ao número {quem_remover} [red]removido com sucesso[/]')

def buscar_animal():
    cabeçalho2('BUSCAR ANIMAL PARA ADOÇÃO')

    nome = console.input('[green]Nome (Ou Enter para pular): [/]').strip().lower()
    especie = console.input('[green]Espécie (Ou Enter para pular): [/]').strip().lower()
    raca = console.input('[green]Raça (Ou Enter para pular): [/]').strip().lower()
    cor = console.input('[green]Cor (Ou Enter para pular): [/]').strip().lower()
    porte = console.input('[green]Porte (Ou Enter para pular): [/]').strip().lower()
    idade = console.input('[green]Idade (Ou Enter para pular): [/]').strip().lower()

    try:
        arquivo = open(arq_animais, 'rt')
    except:
        console.print('Erro ao abrir o arquivo!')
    else:
        encontrados = False
        contador = 1

        cabeçalho2('RESULTADOS DA BUSCA')

        for linha in arquivo:
            dado = linha.strip().split(';')

            nome_animal = dado[0].lower()
            especie_animal = dado[1].lower()
            raca_animal = dado[2].lower()
            cor_animal = dado[3].lower()
            porte_animal = dado[4].lower()
            idade_animal = dado[5].lower()

            if ((nome == '' or nome in nome_animal) and
                (especie == '' or especie in especie_animal) and
                (raca == '' or raca in raca_animal) and
                (cor == '' or cor in cor_animal) and
                (porte == '' or porte in porte_animal) and
                (idade == '' or idade in idade_animal)):

                console.print(f'{contador}. Nome: {dado[0]} | Espécie: {dado[1]} | Raça: {dado[2]} | Cor: {dado[3]} | Porte: {dado[4]} | Idade: {dado[5]} anos | Observação: {dado[6]}')

                encontrados = True

            contador += 1

        if not encontrados:
            console.print('[yellow]Nenhum animal encontrado com essas características.[/]')

        arquivo.close()