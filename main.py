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

# Soma das peças dos jogadores
def soma_pecas(pecas_jogador):
    soma = 0
    for p in pecas_jogador:
        soma += p[0]
        soma += p[1]
    
    return soma

# Possíveis posições na mesa
def posicoes_possiveis(mesa, pecas):
    posicoes = []
    if len(mesa) == 0: # mesa vazia
        for i in range(len(pecas)):
            posicoes.append(i)
        return posicoes

    p1 = mesa[0][0]  # Uma das pontas da mesa
    p2 = mesa[-1][1] # A outra ponta da mesa

    for c in range(len(pecas)):
        if pecas[c][0] == p1 or pecas[c][0] == p2 or pecas[c][1] == p1 or pecas[c][1] == p2:
            posicoes.append(c)
    return posicoes


#---------------------------------------------------------------#

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


#----------------------------------------------------------------#



