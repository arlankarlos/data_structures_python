# tabu search knapsack problem in Python
"""
    configuração da mochila
    para cada sublista, o primeiro elemento é o peso e o
    segundo elemento é o benefício do objeto
"""
import random


mochila = [[4, 2], [5, 2], [7, 3], [9, 4], [6, 4]]  # configuração mochila
iteracao, melhor_iteracao = 0, 0  # iteração atual e melhor iteração
melhor_solucao = []  # guarda a melhor solução encontrada
lista_tabu = []  # guarda as soluções tabu
capacidade_maxima = 20  # capacidade da mochila
bt_max = 1  # número máximo de iterações sem melhora
max_vizinhos = 5  # número máximo de vizinhos

# gera uma solução inicial aleatória
for i in range(len(mochila)):
    bit = random.randint(0, 1)
    melhor_solucao.append(bit)


# função para obter o valor da função objetivo
def obter_avaliacao(solucao, mochila, capacidade_maxima):
    benficio_total = 0
    peso_total = 0
    for i in range(len(solucao)):
        peso_total += solucao[i] * mochila[i][0]
        benficio_total += solucao[i] * mochila[i][1]
    avaliacao = benficio_total * (1 - max(0, peso_total - capacidade_maxima))
    return avaliacao


# função para obter peso de uma solução
def obter_peso(solucao, mochila):
    peso_total = 0
    for i in range(len(solucao)):
        peso_total += solucao[i] * mochila[i][0]
    return peso_total


# função para gerar os vizinhos
def gerar_vizinhos(melhor_solucao, max_vizinhos):
    vizinhos = []
    posicao = 0
    for i in range(max_vizinhos):
        vizinho = []
        for j in range(len(melhor_solucao)):
            if j == posicao:
                if melhor_solucao[j] == 0:
                    vizinho.append(1)
                else:
                    vizinho.append(0)
            else:
                vizinho.append(melhor_solucao[j])
        vizinhos.append(vizinho)
        posicao += 1
    return vizinhos


# função para obter a melhor avaliação de cada vizinho
def obter_avaliacao_vizinhos(vizinhos, mochila, capacidade_maxima, max_vizinhos):
    avaliacoes = []
    for vizinho in vizinhos:
        avaliacao = obter_avaliacao(vizinho, mochila, capacidade_maxima)
        avaliacoes.append(avaliacao)
    return avaliacoes


# função para obter o bit modificado
def obter_bit_modificado(melhor_solucao, melhor_vizinho):
    for i in range(len(melhor_solucao)):
        if melhor_solucao[i] != melhor_vizinho[i]:
            return i


# função para obter vizinho com a máxima avaliação
def obter_vizinho_melhor_avaliação(
    vizinhos_avaliacao, lista_tabu, melhor_solucao, vizinhos
):
    max_avaliacao = max(vizinhos_avaliacao)
    posicao = 0
    bit_proibido = -1

    # verifica se a lista tabu não possui elementos
    if len(lista_tabu) != 0:
        # se possuir, é porque tem bit proibido, então pega esse bit
        bit_proibido = lista_tabu[0]

    # iteração para obter a posição do melhor vizinho
    for i in range(len(vizinhos_avaliacao)):
        if vizinhos_avaliacao[i] == max_avaliacao:
            posicao = i
            break

    # verifica se o vizinho é resultado de movimento proibido
    if bit_proibido != -1:

        # obtem posição do bit que foi modificado para gerar esse vizinho
        bit_pos = obter_bit_modificado(melhor_solucao, vizinhos[posicao])

        # verifica se o bit está na lista tabu
        if bit_pos == bit_proibido:

            # se cair aqui, então procura o segundo melhor vizinho
            melhor_pos = 0

            for i in range(len(vizinhos_avaliacao)):
                if i != bit_pos:
                    if vizinhos_avaliacao[i] > vizinhos_avaliacao[melhor_pos]:
                        melhor_pos = i
            # retorna a posição do segundo melhor vizinho
            return melhor_pos
    # retorna a posição do melhor vizinho
    return posicao


# mostra solução inicial e seu valor de avaliação
print(
    f"Solução inicial: {melhor_solucao}, Avaliação: {obter_avaliacao(melhor_solucao, mochila, capacidade_maxima)}"
)

# obter o peso corrente da mochila
peso_corrente = obter_peso(melhor_solucao, mochila)

# obter o valor de avalição da melhor solução
melhor_avaliacao = obter_avaliacao(melhor_solucao, mochila, capacidade_maxima)

# gerar os vizinhos
vizinhos = gerar_vizinhos(melhor_solucao, max_vizinhos)

# calcular a avaliação dos vizinhos
vizinhos_avaliacao = obter_avaliacao_vizinhos(
    vizinhos, mochila, capacidade_maxima, max_vizinhos
)

# obtem a posição do melhor vizinho
posicao_melhor_vizinho = obter_vizinho_melhor_avaliação(
    vizinhos_avaliacao, lista_tabu, melhor_solucao, vizinhos
)

# verifica se o melhor vizinho tem avalição melhor do que a avalição até o momento
if vizinhos_avaliacao[posicao_melhor_vizinho] > melhor_avaliacao:

    # obtem o bit que foi modificado do melhor vizinho
    bit_modificado = obter_bit_modificado(
        melhor_solucao, vizinhos[posicao_melhor_vizinho]
    )

    # guarda o movimento proibido na lista tabu
    lista_tabu.append(bit_modificado)

    # faz uma cópia da solução
    melhor_solucao = vizinhos[posicao_melhor_vizinho][:]

    # incrementa a iteração onde foi achada a melhor solução até o momento
    melhor_iteracao += 1

iteracao += 1

# entrar em loop
while True:

    """
    A condição de parada é se a diferença entre a iteracao é a melhor_iteracao
    for maior que bt_max. A iteracao é a iteração global (sempre é incrementada).
    melhor_iterecao é a iteração onde se achou a melhor solução (nem sempre é incrementada).
    bt_max é o número máximo de iterações sem melhora no valor da melhor solução.
    """
    if (iteracao - melhor_iteracao) > bt_max:
        break

    # gera os novos vizinhos
    vizinhos = gerar_vizinhos(melhor_solucao, max_vizinhos)

    # obtem o valor de avaliação dos vizinhos
    vizinhos_avaliacao = obter_avaliacao_vizinhos(
        vizinhos, mochila, capacidade_maxima, max_vizinhos
    )

    # obtem a posição do melhor vizinho
    posicao_melhor_vizinho = obter_vizinho_melhor_avaliação(
        vizinhos_avaliacao, lista_tabu, melhor_solucao, vizinhos
    )

    # verifica se o melhor vizinho tem avalição melhor do que a avalição até o momento
    if vizinhos_avaliacao[posicao_melhor_vizinho] > melhor_avaliacao:

        # obtem o bit que foi modificado para gerar o melhor vizinho
        bit_modificado = obter_bit_modificado(
            melhor_solucao, vizinhos[posicao_melhor_vizinho]
        )

        # guarda o movimento proibido na lista tabu
        lista_tabu[0] = bit_modificado

        # faz uma cópia da solução
        melhor_solucao = vizinhos[posicao_melhor_vizinho][:]

        # atualiza a melhor avalização
        melhor_avaliacao = vizinhos_avaliacao[posicao_melhor_vizinho]

        # incrementa a iteração onde foi achada a melhor solução até o momento
        melhor_iteracao += 1
    iteracao += 1


# mostra solução final e seu valor de avaliação
print(
    f"Solução final: {melhor_solucao}, Avaliação: {obter_avaliacao(melhor_solucao, mochila, capacidade_maxima)}"
)
print(f'Melhor iteração: {melhor_iteracao}')
print(f'Iteração: {iteracao}')