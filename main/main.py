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
        opção_1()
    elif resposta == 2:
        lista_animais()
        print(linha())
        remover_animal()
    elif resposta == 3:
        opção_3()
    elif resposta == 4:
        lerArquivo_adotante(arq_adotante)
        print(linha())
        remover_adotante()
    elif resposta == 5:
        lista_animais(arq_animais)
    elif resposta==6:
        lerArquivo_adotante(arq_adotante)
    elif resposta == 7:
        buscar_animal()
    elif resposta == 8:
        cabeçalho('Saindo so sistema... até logo!')
        break
    else:
        print('[red]ERRO! Digite uma opção válida![/]')

    print(continuar())
    opc = Console.input('[green]Sua opção: [/]')
    if opc == '':
        pass

    sleep(1)