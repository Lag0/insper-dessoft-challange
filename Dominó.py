# Importando funções e bibliotecas

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
        print(chalk.red('Número inválido, favor escolher um número entre 2 e 4!'))
    else:
        flag = False

pecas = cria_pecas()
inicia = inicia_jogo(n_jogadores, pecas)
mesa = inicia['mesa']
jogadores_pecas = inicia['jogadores']
monte = inicia['monte']

ordem = np.arange(0, n_jogadores)
random.shuffle(ordem)

print(f'No jogo temos: \n{n_jogadores} jogadores com 7 peças cada!\n')

# Função de formatação do jogo
game_on = True
while game_on:
    for i in ordem:
        def formata():
            
            print(chalk.blue(f'Tamanho do monte: {len(monte)} peças'))
            print(chalk.yellow(f"Mesa Atual: {mesa}\n"))

            print("-"*30)

            print(chalk.green(f'Jogador {i}:'))
            print(chalk.magenta(jogadores_pecas[i]))

            print("-"*30)
            
            if len(posicoes_possiveis(mesa, jogadores_pecas[i])) >= 1:
                print("\nPosições Possiveis: ")
                print(posicoes_possiveis(mesa, jogadores_pecas[i])) 

                jogar = int(input('Qual peça você quer jogar: '))
                adiciona_na_mesa(jogadores_pecas[i][jogar], mesa)
                jogadores_pecas[i].pop(jogar)

            # COMPRA DO MONTE!
            compra_monte = 0
            while len(posicoes_possiveis(mesa, jogadores_pecas[i])) == 0 and len(jogadores_pecas[i]) > 0:
                user_input = input(
                    chalk.red.bold(
                        '\nVocê não tem peças possiveis! Aperte [ENTER] para comprar do monte!\n'
                    )
                )

                if user_input == '':
                    jogadores_pecas[i].append(monte[0])
                    monte.pop(0)
                    compra_monte += 1
                else:
                    print(chalk.red.bold("Opção Invalida! Precisione a tecla [ENTER]\n"))
                print(chalk.red(f"Você comprou {compra_monte} peças nessa rodada\n"))
                
            if len(monte) == 0 and len(posicoes_possiveis(mesa, jogadores_pecas[i])) == 0:
                for c in ordem:
                    pontuacao = soma_pecas(jogadores_pecas[c])
                quit()
                
            if len(jogadores_pecas[i]) == 0:
                print(chalk.green(f"Jogo acabou! \nO ganhador foi o jogador {i}!!"))
                quit()
                
        formata()




