# graph generator in Python
# import sys, time
import random


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
                print(f"Best solution: {best_solution} with evaluation {best_eval}")
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

    def pcv_genectic(self, population_len, generate, turn_len, crossover, mutation):
        population = []

        def generate_solution():

            vertice = [i for i in range(1, self.vertices)]
            solution = [0]

            while len(vertice) > 0:
                vertex = random.choice(vertice)
                vertice.remove(vertex)
                solution.append(vertex)

            return solution

        # função de fitness
        def get_evaluation(solution):
            eval = 0
            for i in range(self.vertices - 1):
                eval += self.weights[(solution[i], solution[i + 1])]
            eval += self.weights[(solution[-1], solution[0])]
            return eval

        # gerar a população inicial
        for i in range(population_len):
            population.append(generate_solution())

        # a cada geração
        for i in range(generate):

            # a seleção por torneio
            for j in range(turn_len):

                if random.random() <= crossover:
                    # crossover
                    ind1, ind2 = None, None

                    # selecionar dois individuos diferentes
                    while True:
                        ind1 = random.randint(0, population_len - 1)
                        ind2 = random.randint(0, population_len - 1)
                        if ind1 != ind2:
                            break

                    gen1_valid = [i for i in range(self.vertices)]
                    gen2_valid = gen1_valid[:]
                    gen1, gen2 = [], []

                    # crossover
                    while True:
                        # selecionar um ponto
                        cut = random.randint(0, self.vertices - 1)

                        # não seleciona as extremidades
                        if cut != 0 and cut != (self.vertices - 1):

                            for p in range(cut):

                                if population[ind1][p] in gen1_valid:
                                    gen1.append(population[ind1][p])
                                    gen1_valid.remove(population[ind1][p])
                                else:
                                    e = random.choice(gen1_valid)
                                    gen1.append(e)
                                    gen1_valid.remove(e)

                                if population[ind2][p] in gen2_valid:
                                    gen2.append(population[ind2][p])
                                    gen2_valid.remove(population[ind2][p])
                                else:
                                    e = random.choice(gen2_valid)
                                    gen2.append(e)
                                    gen2_valid.remove(e)

                            for p in range(cut, self.vertices):
                                if population[ind2][p] in gen1_valid:
                                    gen1.append(population[ind2][p])
                                    gen1_valid.remove(population[ind2][p])
                                else:
                                    e = random.choice(gen1_valid)
                                    gen1.append(e)
                                    gen1_valid.remove(e)

                                if population[ind1][p] in gen2_valid:
                                    gen2.append(population[ind1][p])
                                    gen2_valid.remove(population[ind1][p])
                                else:
                                    e = random.choice(gen2_valid)
                                    gen2.append(e)
                                    gen2_valid.remove(e)

                            # print(cut)
                            # print(f"Pai 1: {population[ind1]}")
                            # print(f"Pai 2: {population[ind2]}")
                            # print(f"Gen 1: {gen1}")
                            # print(f"Gen 2: {gen2}")
                            # sys.exit(1)
                            break

                    # aplica operador de mutação
                    if random.random() <= mutation:
                        m1, m2 = None, None
                        # mutação
                        # print("Mutação")
                        # print(f"Gen 1: {gen1}")
                        # print(f"Gen 2: {gen2}")
                        # print()
                        while True:
                            m1 = random.randint(0, self.vertices - 1)
                            m2 = random.randint(0, self.vertices - 1)
                            if m1 != m2:
                                gen1[m1], gen1[m2] = gen1[m2], gen1[m1]
                                gen2[m1], gen2[m2] = gen2[m2], gen2[m1]
                                break

                    # obtém o fitness de cada individuo
                    fitness_ind1 = get_evaluation(population[ind1])
                    fitness_ind2 = get_evaluation(population[ind2])
                    fitness_gen1 = get_evaluation(gen1)
                    fitness_gen2 = get_evaluation(gen2)

                    if fitness_gen1 < fitness_ind1 or fitness_gen1 < fitness_ind2:
                        if fitness_gen1 < fitness_ind1:
                            population.pop(ind1)
                        else:
                            population.pop(ind2)
                        population.append(gen1)
                    elif fitness_gen2 < fitness_ind1 or fitness_gen2 < fitness_ind2:
                        if fitness_gen2 < fitness_ind1:
                            population.pop(ind1)
                        else:
                            population.pop(ind2)
                        population.append(gen2)

        # obtém o melhor individuo da população
        melhor_individuo = population[0][:]
        print('Best gen: %s - Custo: %d' %(str(melhor_individuo), get_evaluation(melhor_individuo)))
        for individuo in range(1, population_len):
            if get_evaluation(population[individuo]) < get_evaluation(melhor_individuo):
                melhor_individuo = population[individuo][:]

        print(
            "Best gen: %s - Custo: %d"
            % (str(melhor_individuo), get_evaluation(melhor_individuo))
        )


gerador = GraphGenerator(50)
gerador.graph_generator()
print("RANDOM")
gerador.pcv_random(1000)
print()
print("GENETIC ALGORITHM")
gerador.pcv_genectic(
    population_len=75, generate=1000, turn_len=25, crossover=0.7, mutation=0.1
)
