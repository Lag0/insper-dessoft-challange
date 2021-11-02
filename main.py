# COMECANDO O CODIGO

# Criando as peças do jogo

import random

def cria_pecas():
    pecas = []

    i = 0
    while i <= 6:

        a = 0
        while a <= 6:
            if [i, a] not in pecas and [a, i] not in pecas:
                pecas.append[i, a]
            a += 1
            
        i += 1
    
    random.shuffle(pecas)
    return pecas


