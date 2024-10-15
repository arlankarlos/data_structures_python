# graph -- adjacency matrix undirected -- in Python

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0] * vertices for column in range(vertices)]
        self.visited = [False] * self.vertices
        
    def add_arcs(self, u, v):
        self.graph[u-1][v-1] = 1
        self.graph[v-1][u-1] = 1
        
    def show(self):
        for i in self.graph:
            for j in i:
                print(j, end = " ")
            print('')
            
    def has_arc(self, u, v):
        if self.graph[u-1][v-1] == 1:
            return True
        else:
            return False
        
    def dfs(self, u):
        self.visited[u-1] = True
        print(f"{u} visitado")
        for i in range(1, self.vertices+1):
            if self.graph[u-1][i-1] == 1 and not self.visited[i-1]:
                self.dfs(i)
                
    def bfs(self, v):
        
        # lista de visitados
        visited = [False] * self.vertices
        # marca 'v' como visitado
        visited[v-1] = True
        # insere 'v' na fila
        queue = [v-1]
        print(f"{v} visitado")
        
        # enquanto a fila não for vazia
        while queue:
            # obtem o primeiro elemento da fila e o remove
            v = queue[0]
            
            # para cada vértice 'u' adjacentes a 'v'
            for u in range(self.vertices):
                # verifica se existe conexão e se 'u' não foi visitado
                if self.graph[v][u] == 1 and not visited[u]:
                    # insere 'u' na fila
                    queue.append(u)
                    # marca 'u' como visitado
                    visited[u] = True
                    # imprime elemento visitado
                    print(f"{u+1} visitado")
            # remove 'v' da fila
            queue.pop(0)


graph = Graph(5)
graph.add_arcs(1, 3)
graph.add_arcs(3, 4)
graph.add_arcs(2, 3)
graph.add_arcs(3, 5)
graph.add_arcs(4, 5)

graph.show()
print(graph.has_arc(1, 3))
print(graph.has_arc(1, 5))

print('DFS:')
graph.dfs(1)
print()

dfs_graph = Graph(5)
dfs_graph.add_arcs(1, 4)
dfs_graph.add_arcs(4, 2)
dfs_graph.add_arcs(4, 5)
dfs_graph.add_arcs(2, 5)
dfs_graph.add_arcs(5, 3)

print('DFS:')
dfs_graph.dfs(1)

bfs_graph = Graph(10)
bfs_graph.add_arcs(1, 2)
bfs_graph.add_arcs(1, 3)
bfs_graph.add_arcs(1, 4)
bfs_graph.add_arcs(2, 5)
bfs_graph.add_arcs(3, 6)
bfs_graph.add_arcs(3, 7)
bfs_graph.add_arcs(4, 8)
bfs_graph.add_arcs(5, 9)
bfs_graph.add_arcs(6, 10)

print('BFS:')
bfs_graph.bfs(1)