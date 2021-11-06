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

            if i != 0:
                print(chalk.green(f'Jogador {i} com {len(jogadores_pecas[i])} peças: '))
            else:
                print(chalk.green(f'Jogador {0} com {len(jogadores_pecas[0])} peças: '))
                print(chalk.magenta(jogadores_pecas[0]))

            print("-"*30)
            
            if len(posicoes_possiveis(mesa, jogadores_pecas[i])) >= 1 and i == 0:
                print("\nPosições das peças possíveis: ")
                print(posicoes_possiveis(mesa, jogadores_pecas[i])) 


            if i == 0:
                jogar = int(input('Qual peça você quer jogar: '))
                adiciona_na_mesa(jogadores_pecas[i][jogar], mesa)
                jogadores_pecas[i].pop(jogar)
            else:
                a = posicoes_possiveis(mesa,jogadores_pecas[i])
                if len(a) > 0:
                    print(f'{jogadores_pecas[i]}\n')
                    adiciona_na_mesa(jogadores_pecas[i][a[0]], mesa)
                    jogadores_pecas[i].pop(a[0])
                else:
                    compra_monte2 = 0
                    f = True
                    while f: # Esse while não está funcionando - Quando o robo tira a peça que é possível de jogar o loop, porém ele não joga a peça possível na mesa
                        if len(posicoes_possiveis(mesa, jogadores_pecas[i])) == 0 and len(jogadores_pecas[i]) > 0:
                            jogadores_pecas[i].append(monte[0])
                            monte.pop(0)
                            compra_monte2 += 1

                            print(chalk.red(f"O Jogador {i} comprou {compra_monte2} peça(s) nessa rodada"))
                            print(f'{jogadores_pecas[i]}\n')
                        else: 
                            adiciona_na_mesa(jogadores_pecas[i][a[0]], mesa) # Por causa do else esse a só pode ser igual a 0 - PROBLEMA
                            jogadores_pecas[i].pop(a[0])
                            f = False

                    
                    

            # COMPRA DO MONTE!
            compra_monte = 0
            while len(posicoes_possiveis(mesa, jogadores_pecas[0])) == 0 and len(jogadores_pecas[0]) > 0: # Apenas o jogador manual deve apertar ENTER para comprar peças
                user_input = input(
                    chalk.red.bold(
                        '\nVocê não tem peças possiveis! Aperte [ENTER] para comprar do monte!\n'
                    )
                )

                if user_input == '':
                    jogadores_pecas[0].append(monte[0])
                    monte.pop(0)
                    compra_monte += 1
                else:
                    print(chalk.red.bold("Opção Invalida! Precisione a tecla [ENTER]\n"))
                print(chalk.red(f"Você comprou {compra_monte} peça(s) nessa rodada\n"))
                
            if len(monte) == 0 and len(posicoes_possiveis(mesa, jogadores_pecas[i])) == 0:
                for c in ordem:
                    pontuacao = soma_pecas(jogadores_pecas[c])

                    print(chalk.green(f"No desempate, o ganhador foi o jogador {i}!!")) # Precisa de ajuste

                quit()
                
            if len(jogadores_pecas[i]) == 0:
                print(chalk.green(f"Jogo acabou! \nO ganhador foi o jogador {i}!!"))
                quit()
                
        formata()




