from rich import print
from interface import *
from libArquivo import *

arq_animais = 'animais.txt'
arq_adotante = 'adotante.txt'

def opc3():
    cabeçalho('NOVO CADASTRADO')
    nome = input('Nome: ')
    idade = int(input('idade: '))
    cpf = input('CPF[xxx.xxx.xxx-xx]: ')
    nascimento = input('Data de nascimento[xx/xx/xxxx]: ')
    endereço = input('Endereço: ')
    cidade = input('Cidade: ')
    estado = input('Estado: ')
    cadastrar_adotante(arq_adotante,nome,idade,cpf,nascimento,endereço,cidade,estado)