# graph generator in Python
import random
import time


class GraphGenerator:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for column in range(vertices)]
        self.weights = {}

    def graph_generator(self):
        """
        Function to generate a graph.
        """
        for i in range(self.vertices):
            for j in range(self.vertices):
                if i != j:
                    if (i, j) and (j, i) not in self.weights:
                        weight = random.randint(1, 100)
                        self.weights[(i, j)] = weight
                        self.weights[(j, i)] = weight
                    self.graph[i].append(j)

    def print_graph(self):
        """
        Function to print the graph.
        """
        for i in range(self.vertices):
            print(f"Vertex {i}:", end=" ")
            for vertex in self.graph[i]:
                print(f"(weight {self.weights[i, vertex]}) -> {vertex} -> ", end=" ")
            print()

    def pcv_random(self, iterations):
        best_solution = []
        best_eval = None

        def random_solution(best_solution, best_eval):

            vertice = [i for i in range(1, self.vertices)]
            solution = [0]
            eval = 0

            while len(vertice) > 0:
                vertex = random.choice(vertice)
                vertice.remove(vertex)
                eval += self.weights[(solution[-1], vertex)]
                solution.append(vertex)

            eval += self.weights[(solution[-1], 0)]

            if best_eval is None:
                best_solution = solution[:]
                best_eval = eval
                print(f"Best solution: {best_solution} with evaluation {best_eval}\n")
            else:
                if eval < best_eval:
                    best_solution = solution[:]
                    best_eval = eval

            return (best_solution, best_eval)

        for i in range(iterations):
            best_solution, best_eval = random_solution(best_solution, best_eval)
            # print(f"Iteration {i + 1}:")
            # print(f"Best solution: {best_solution} with evaluation {best_eval}\n")
            # time.sleep(0.01)
        print(f"Best solution: {best_solution} with evaluation {best_eval}\n")


gerador = GraphGenerator(10)
gerador.graph_generator()
# gerador.print_graph()
gerador.pcv_random(1000000)
