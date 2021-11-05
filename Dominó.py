# Importando funções e bibliotecas

import pprint
from random import *
from main import *
import numpy as np  

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

ordem = np.arange(0, n_jogadores)
random.shuffle(ordem)
print(ordem)



print(f'No jogo temos: \n{n_jogadores} jogadores com 7 peças cada!\n')


# Função de formatação do jogo
while True:
    def formata():
        print(f'Tamanho do monte: {len(monte)} peças')
        print(f"Mesa Atual: {mesa}")
        print('Jogador 0: ')
        print(jogadores_pecas[0])
        print(posicoes_possiveis(mesa, jogadores_pecas[0]))
        jogar = int(input('Qual peça você quer jogar: '))
        adiciona_na_mesa(jogadores_pecas[0][jogar], mesa)
        jogadores_pecas[0].pop(jogar)
        print(f"Mesa Atual: {mesa}")

    formata()
    #for i in range(len(ordem)):
        #print(f'Jogador {ordem[i]}: ')
    


