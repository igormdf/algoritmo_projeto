from interface import *
from time import sleep
from rich import print
from lib_adotante import *
from lib_animal import *
from lib_arquivo import *

arq_animais = 'animais.txt'
arq_adotante = 'adotante.txt'

if not arquivoExiste(arq_animais):
    criarArquivo(arq_animais)

if not arquivoExiste(arq_adotante):
    criarArquivo(arq_adotante)

while True:
    resposta = menu()
    if resposta == 1:
        adicionar_animal()
    elif resposta == 3:
        opção_3()
    elif resposta == 4:
        lerArquivo_adotante(arq_adotante)
        print(linha())
        quem_remover = input('Escolha o número de quem remover: ')
        remover_adotante(quem_remover)
    elif resposta == 5:
        lista_animais(arq_animais)
    elif resposta==6:
        lerArquivo_adotante(arq_adotante)
    elif resposta == 8:
        cabeçalho('Saindo so sistema... até logo!')
        break
    else:
        print('[red]ERRO! Digite uma opção válida![/]')
    sleep(2)









#   Sistema de Adoção de Pets: Cadastro de animais em um abrigo
#(nome, espécie, raça, cor, porte, idade, observações) e perfis de
#adotantes (cpf, nome, data de nascimento, endereço, cidade, estado). O
#menu deverá dispor, pelo menos, das seguintes opções: Adicionar animal,
#remover animal, adicionar adotante, remover adotante, listar animais,
#listar adotantes, buscar animal para adoção