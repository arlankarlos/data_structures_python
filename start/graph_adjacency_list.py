# graph -- adjacency list -- in Python


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for column in range(vertices)]
        
    def add_arcs(self, u, v):
        self.graph[u-1].append(v-1)
        
    def show(self):
        for i in range(self.vertices):
            print(f"{i+1}", end=' ')
            for j in self.graph[i]:
                print(f"{j+1}->", end=' ')
            print('')
            
graph = Graph(5)
graph.add_arcs(1, 2)
graph.add_arcs(4, 1)
graph.add_arcs(2, 3)
graph.add_arcs(2, 5)
graph.add_arcs(5, 3)

graph.show()