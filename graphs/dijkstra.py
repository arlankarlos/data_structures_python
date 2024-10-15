# dijkstra algorithm in Python
from collections import defaultdict
import heapq


# min heap
class MinHeap:
    def __init__(self) -> None:
        self._queue = []
        self._index = 0

    def insert(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def remove(self):
        return heapq.heappop(self._queue)[-1]

    def get_length(self):
        return len(self._queue)


# graph
class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)
        self.vertices = {}

    def add_edge(self, source, destination, weight):
        self.graph[source].append((destination, weight))
        self.vertices[source] = source
        self.vertices[destination] = destination

    def dijkstra(self, source, destination):
        # obtem o número de vértices
        number_vertices = len(self.vertices)

        # estimativas de menor custo
        p = [None for i in range(number_vertices)]

        # estima para origem é 0
        p[source] = 0

        # constrói a min heap
        min_heap = MinHeap()

        # insere a origem na min heap
        min_heap.insert(source, 0)

        # enquanto o tamnho da fila for maior que 0
        while min_heap.get_length() > 0:
            # remove o vértice com menor custo
            u = min_heap.remove()

            # percorre todos os vértices adjacentes
            for edge in self.graph[u]:
                # obtem o vértice adjacente e o peso da aresta
                v = edge[0]
                weight = edge[1]

                # relaxamento
                if p[v] is None or p[v] > p[u] + weight:
                    p[v] = p[u] + weight
                    min_heap.insert(v, p[v])

        return p[destination]


graph = Graph()
graph.add_edge(0, 1, 1)
graph.add_edge(0, 3, 3)
graph.add_edge(0, 4, 10)
graph.add_edge(1, 2, 5)
graph.add_edge(2, 4, 1)
graph.add_edge(3, 2, 2)
graph.add_edge(3, 4, 6)

print(graph.dijkstra(0, 4))  # 6