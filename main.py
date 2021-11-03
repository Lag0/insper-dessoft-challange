# COMECANDO O CODIGO

# Criando as peças do jogo

import random 

def cria_pecas():
    pecas = []
    for i in range(7):

        for a in range(7):
            if [i, a] not in pecas and [a, i] not in pecas:
                pecas.append([i, a])
    random.shuffle(pecas)

    return pecas


