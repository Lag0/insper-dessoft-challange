# Importando funções e bibliotecas

import pprint
from random import *
from main import *

# Começando o jogo
flag = True
continuar = True

while flag:
    n_jogadores = int(input('Qual o número o de jogadores [2-4]: '))
    if n_jogadores > 4 or n_jogadores < 2:
        print('Número inválido, favor escolher um número entre 2 e 4!')
    else:
        flag = False
        
pecas = cria_pecas()
inicia = inicia_jogo(n_jogadores, pecas)
mesa = inicia['mesa']
jogadores_pecas = inicia['jogadores']
monte = inicia['monte']

print(f'No jogo temos: \n{n_jogadores} jogadores com 7 peças cada!\n')
print(f'Tamanho do monte: {len(monte)} peças')
print(f"Mesa Atual: {mesa}")

print(f'Jogador {n_jogadores}:')

