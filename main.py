# COMECANDO O CODIGO

# Importações Necessárias
import random

# Criando as peças do jogo
def cria_pecas():
    peças = []
    for i in range(7):
        for a in range(7):
            if [i, a] not in peças and [a, i] not in peças:
                peças.append([i, a])
    random.shuffle(peças)

    return peças

def inicia_jogo(jogadores, peças):
    lista = {'jogadores': {}, 'monte': [], 'mesa': []}
    for i in range(jogadores):
        lista['jogadores'][i] = peças[0:7]
        del peças[0:7]
    lista['monte'] = peças
    return lista

jogadores = 2
peças = cria_pecas()
print(f'Lista Peças: {peças}...')
print(inicia_jogo(jogadores, peças))

