from rich import print
from rich.panel import Panel 

def menu():
    texto = Panel("""[yellow]1[/yellow] - [blue]Adicionar animal[/blue]
[yellow]2[/yellow] - [blue]Remover animal[/blue]
[yellow]3[/yellow] - [blue]Adicionar adotante[/blue]
[yellow]4[/yellow] - [blue]Remover adotante[/blue]
[yellow]5[/yellow] - [blue]Lista de animais[/blue]
[yellow]6[/yellow] - [blue]Lista de adotantes[/blue]
[yellow]7[/yellow] - [blue]Buscar animal para adoção[/blue] 
[yellow]8[/] - [blue]Sair do sistema[/]""", title="Menu Principal",width=34)
    print(texto)
    opc = leiaint('\033[32mSua opção: \033[m')
    return opc 

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def linha(tam = 42):
    return '-' * tam

def leiaint(msg):
    ok = False 
    valor = 0 
    while True:
        n = input(msg)
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('[red]ERRO! Digite um número inteiro válido[/]')
        if ok:
            break
    return valor

def continuar():
    texto = Panel("""[green]Precione enter para voltar para o menu principal [/]""", title="Menu Principal",width=45)
    return texto