from interface import *
from time import sleep
from rich import print
from lib_adotante import *
from lib_animal import *
from lib_arquivo import *
from rich.console import Console

arq_animais = 'animais.txt'
arq_adotante = 'adotante.txt'
Console = Console()

if not arquivoExiste(arq_animais):
    criarArquivo(arq_animais)

if not arquivoExiste(arq_adotante):
    criarArquivo(arq_adotante)

while True:
    resposta = menu()
    if resposta == 1:
        adicionar_animal()
    elif resposta == 2:
        lista_animais()
        print(linha())
        remover_animal()
        print(continuar())
        opc = Console.input('')
    elif resposta == 3:
        adicionar_animal()
        print(continuar())
        opc = Console.input('')
    elif resposta == 4:
        lerArquivo_adotante(arq_adotante)
        print(linha())
        remover_adotante()
        print(continuar())
        opc = Console.input('')
    elif resposta == 5:
        lista_animais(arq_animais)
        print(continuar())
        opc = Console.input('')
    elif resposta==6:
        lerArquivo_adotante(arq_adotante)
        print(continuar())
        opc = Console.input('')
    elif resposta == 7:
        buscar_animal()
        print(continuar())
        opc = Console.input('')
    elif resposta == 8:
        cabeçalho('Saindo so sistema... até logo!')
        break
    else:
        print('[red]ERRO! Digite uma opção válida![/]')

    print(continuar())
    opc = Console.input('')
    if opc == '':
        pass

    sleep(1)