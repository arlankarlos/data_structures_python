class Graph:
    def __init__(self, V) -> None:
        self.V = V
        self.list_adj = [[] for _ in range(V)]

    def add_edge(self, source, destination):
        self.list_adj[source].append(destination)

    def dfs(self, v):
        pile = []
        visited = [False for _ in range(self.V)]
        pile_rec = [False for _ in range(self.V)]

        while True:

            found_neighbor = False

            if not visited[v]:
                pile.append(v)
                visited[v] = pile_rec[v] = True

            aux_neighbor = None
            for neighbor in self.list_adj[v]:
                aux_neighbor = neighbor
                # se o vizinho está na pilha, é porque existe ciclo
                if pile_rec[neighbor]:
                    return True
                elif not visited[neighbor]:
                    # se não está na pilha e não foi visitado, indica que achou
                    found_neighbor = True
                    break

            if not found_neighbor:
                # marca que saiu da pilha
                pile_rec[pile[-1]] = False

                # remove da pilha
                pile.pop()

                if len(pile) == 0:
                    break

                # atualiza o vértice
                v = pile[-1]
            else:
                # atualiza o vértice
                v = aux_neighbor
        return False

    def is_cyclic(self):
        for i in range(self.V):
            if self.dfs(i):
                return True
        return False


graph1 = Graph(3)
graph1.add_edge(0, 1)
graph1.add_edge(1, 2)
graph1.add_edge(2, 0)
print(graph1.is_cyclic())  # True

graph2 = Graph(4)
graph2.add_edge(0, 1)
graph2.add_edge(1, 2)
graph2.add_edge(2, 3)
print(graph2.is_cyclic())  # False
