import random

# Dados do problema
itens = [
    {'peso': 12, 'valor': 4},
    {'peso': 2, 'valor': 2},
    {'peso': 1, 'valor': 1},
    {'peso': 1, 'valor': 2},
    {'peso': 4, 'valor': 10},
    {'peso': 1, 'valor': 2},
    {'peso': 2, 'valor': 1},
    {'peso': 1, 'valor': 1},
    {'peso': 2, 'valor': 2},
    {'peso': 10, 'valor': 15}
]

capacidade_mochila = 15
max_iteracoes = 100
max_iteracoes_sem_melhoria = 20
tamanho_lista_tabu = 5

def calcular_valor(solucao):
    valor_total = 0
    peso_total = 0
    for i in range(len(solucao)):
        if solucao[i] == 1:
            valor_total += itens[i]['valor']
            peso_total += itens[i]['peso']
    return valor_total, peso_total

def gerar_solucao_inicial():
    while True:
        solucao = [random.randint(0, 1) for _ in range(len(itens))]
        valor, peso = calcular_valor(solucao)
        if peso <= capacidade_mochila:
            return solucao

def gerar_vizinhos(solucao_atual):
    vizinhos = []
    for i in range(len(solucao_atual)):
        vizinho = solucao_atual.copy()
        vizinho[i] = 1 - vizinho[i]  # Troca 0 por 1 ou 1 por 0
        valor, peso = calcular_valor(vizinho)
        if peso <= capacidade_mochila:
            vizinhos.append((vizinho, i))
    return vizinhos

def busca_tabu():
    solucao_atual = gerar_solucao_inicial()
    valor_melhor, _ = calcular_valor(solucao_atual)
    melhor_solucao_global = solucao_atual.copy()
    lista_tabu = []
    iteracoes_sem_melhoria = 0

    for iteracao in range(max_iteracoes):
        vizinhos = gerar_vizinhos(solucao_atual)
        melhor_vizinho = None
        valor_melhor_vizinho = float('-inf')
        indice_movimento = -1

        for vizinho, movimento in vizinhos:
            if movimento in lista_tabu:
                # Critério de aspiração
                valor_vizinho, _ = calcular_valor(vizinho)
                if valor_vizinho > valor_melhor:
                    melhor_vizinho = vizinho
                    valor_melhor_vizinho = valor_vizinho
                    indice_movimento = movimento
            else:
                valor_vizinho, _ = calcular_valor(vizinho)
                if valor_vizinho > valor_melhor_vizinho:
                    melhor_vizinho = vizinho
                    valor_melhor_vizinho = valor_vizinho
                    indice_movimento = movimento

        if melhor_vizinho is None:
            break  # Nenhum vizinho disponível

        solucao_atual = melhor_vizinho
        lista_tabu.append(indice_movimento)
        if len(lista_tabu) > tamanho_lista_tabu:
            lista_tabu.pop(0)

        if valor_melhor_vizinho > valor_melhor:
            melhor_solucao_global = melhor_vizinho.copy()
            valor_melhor = valor_melhor_vizinho
            iteracoes_sem_melhoria = 0
        else:
            iteracoes_sem_melhoria += 1

        if iteracoes_sem_melhoria >= max_iteracoes_sem_melhoria:
            break

        # Debug: Exibir o progresso
        print(f"Iteração {iteracao+1}: Melhor Valor = {valor_melhor}")

    return melhor_solucao_global, valor_melhor

# Executar o algoritmo
melhor_solucao, valor_melhor_solucao = busca_tabu()
peso_melhor_solucao = calcular_valor(melhor_solucao)[1]

# Exibir os resultados
print("\nMelhor Solução Encontrada:")
print(f"Itens Selecionados: {melhor_solucao}")
print(f"Valor Total: {valor_melhor_solucao}")
print(f"Peso Total: {peso_melhor_solucao}")
print("Itens na Mochila:")
for i in range(len(melhor_solucao)):
    if melhor_solucao[i] == 1:
        print(f"- Item {i+1}: Peso = {itens[i]['peso']}, Valor = {itens[i]['valor']}")
