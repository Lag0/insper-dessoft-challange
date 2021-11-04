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

def adiciona_na_mesa(peca, mesa):
    if len(mesa) == 0:
        mesa.append(peca)
        return mesa

    p1 = peca[0] # primeiro número da peça
    p2 = peca[1] # segundo número da peca

    mesa1 = mesa[0][0] # primeiro número da primeira peça
    mesa2 = mesa[-1][1] # Último número da última peça

    if p1 == mesa1:
        inv = [p2, p1]
        mesa.insert(0, inv) # Peça invertida na mesa

    elif p2 == mesa1:
        mesa.insert(0, peca) # Peça na posição original na mesa

    elif p1 == mesa2:
        mesa.append(peca) # Peca no final da mesa

    elif p2 == mesa2:
        inv = [p2, p1]
        mesa.append(inv) # Peça invertida na mesa
        
    return mesa

#---------------------------------------------------------------#
#                       IGNORE - TEST ONLY                      #
jogadores = 3
peças = cria_pecas()
dicionario = (inicia_jogo(jogadores, peças))
pecas_testes = dicionario['jogadores'][0]
pecas_testes2 = dicionario['jogadores'][0][1]
#                       SOMENTE PARA TESTE                      #
#---------------------------------------------------------------#



