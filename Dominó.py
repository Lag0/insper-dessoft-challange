# Importando funções e bibliotecas

from random import*
from main import*

# Começando o jogo
flag = True
while flag:
    n_jogadores = int(input('Qual o número o de jogadores: '))
    if n_jogadores > 4 or n_jogadores < 2:
        print('Número inválido, escolher um número entre 2 e 4')
    elif n_jogadores <= 4 and n_jogadores >= 2:
        flag = False

pecas = cria_pecas()


a = inicia_jogo(n_jogadores, pecas)
print(a)

