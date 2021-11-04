# Importando funções e bibliotecas

import pprint
from random import *
from main import *

# Começando o jogo
flag = True
while flag:
    n_jogadores = int(input('Qual o número o de jogadores: '))
    if n_jogadores > 4 or n_jogadores < 2:
        print('Número inválido, favor escolher um número entre 2 e 4!')
    else:
        flag = False

pecas = cria_pecas()
inicia = inicia_jogo(n_jogadores, pecas)

pprint.pprint(inicia)

