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
        while True:
            adicionar_animal()
            loop()
            opçao = Console.input('[green]Sua opção: [/]').lower()
            if opçao == "v":
                break

    elif resposta == 2:
        while True:
            lista_animais()
            print(linha())
            remover_animal()
            loop()
            opçao = Console.input('[green]Sua opção: [/]').lower()
            if opçao == "v":
                break

    elif resposta == 3:
        while True:
            adicionar_adotante()
            loop()
            opçao = Console.input('[green]Sua opção: [/]').lower()
            if opçao == "v":
                break

    elif resposta == 4:
        while True:
            lerArquivo_adotante(arq_adotante)
            print(linha())
            remover_adotante()
            loop()
            opçao = Console.input('[green]Sua opção: [/]').lower()
            if opçao == "v":
                break

    elif resposta == 5:
        lista_animais(arq_animais)
        print(continuar())
        opc = Console.input('')

    elif resposta==6:
        lerArquivo_adotante(arq_adotante)
        print(continuar())
        opc = Console.input('')

    elif resposta == 7:
        while True:
            buscar_animal()
            loop()
            opçao = Console.input('[green]Sua opção: [/]').lower()
            if opçao == "v":
                break

    elif resposta == 8:
        cabeçalho2('Saindo do sistema... Até logo!')
        break

    else:
        print('[red]ERRO! Digite uma opção válida![/]')
    sleep(1)