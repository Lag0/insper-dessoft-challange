# Importando funções e bibliotecas

import pprint
from random import *
from main import *
import numpy as np 
from yachalk import chalk

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
while len(jogadores_pecas[0]) > 0:
    def formata():
        
        print(chalk.blue(f'Tamanho do monte: {len(monte)} peças'))
        print(chalk.yellow(f"Mesa Atual: {mesa}\n"))
        
        print("-"*30)
        
        print(chalk.green('Jogador 0:'))
        print(chalk.magenta(jogadores_pecas[0]))
        
        print("-"*30)
        
        print("\nPosições Possiveis: ")
        print(posicoes_possiveis(mesa, jogadores_pecas[0]))
        
        jogar = int(input('Qual peça você quer jogar: '))
        adiciona_na_mesa(jogadores_pecas[0][jogar], mesa)
        jogadores_pecas[0].pop(jogar)
        
        print(f"\nMesa Atual: {mesa}\n")
        
        # COMPRA DO MONTE!
        compra_monte = 0
        while len(posicoes_possiveis(mesa, jogadores_pecas[0])) == 0 and len(jogadores_pecas[0]) > 0:
            jogadores_pecas[0].append(monte[0])
            monte.pop(0)
            compra_monte += 1
            print(chalk.red.bold(f"\nVocê não tem peças! Comprou {compra_monte} peças do monte! \n"))
    formata()




