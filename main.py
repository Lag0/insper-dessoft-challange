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

# Iniciando o Jogo
def inicia_jogo(jogadores, peças):
    dicionario = {'jogadores': {}, 'monte': [], 'mesa': []}
    for i in range(jogadores):
        dicionario['jogadores'][i] = peças[0:7]
        del peças[0:7]
    dicionario['monte'] = peças
    return dicionario

# Verificando Ganhador
def verifica_ganhador(dicionario):
    for k in dicionario.keys():
        if dicionario[k] == []:
            return k
    else: return -1

# IGNORE - TEST ONLY
jogadores = 4
peças = cria_pecas()
dicionario = (inicia_jogo(jogadores, peças))
print(verifica_ganhador(
                        {
                        0: [[1, 3], [0, 1], [4, 6], [0, 3], [0, 4], [6, 6], [0, 6]], 
                        1: [], 
                        2: [[3, 6], [2, 4], [2, 5], [2, 6], [3, 3], [3, 4], [2, 3]], 
                        3: [[3, 5], [4, 4], [4, 5], [0, 2], [5, 5], [5, 6], [0, 5]]
                        }))

