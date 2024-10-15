# one max in Python
# solved using simulated annealing
import random
import math


class OneMax:
    def __init__(self, size) -> None:
        self.size = size
        self.solution = [random.randint(0, 1) for _ in range(size)]
        self.weight = self.objective_function(self.solution)

    def neighbor(self) -> list:
        new_neighbor = self.solution[:]
        position = random.randint(0, self.size - 1)
        new_neighbor[position] = 1 if new_neighbor[position] == 0 else 0
        return new_neighbor

    # função objetivo
    def objective_function(self, solution) -> int:
        return sum(solution)

    """
        Simulated Annealing
        T -> temperatura inicial
        T-min -> temperatura mínima
        alpha -> fator de redução (decaimento) da temperatura
        max_iter -> número máximo de iterações com a mesma temperatura
    """

    def run_annealing(self, T=1.0, T_min=0000.1, alpha=0.9, max_iter=100):
        while T > T_min:

            # iterações com uma mesma temperatura
            for i in range(max_iter):
                # gera uma nova solução
                new_solution = self.neighbor()
                # calcula o custo dessa nova solução
                new_weight = self.objective_function(new_solution)
                # calcula a diferença dos custos
                delta = self.weight - new_weight
                # probabilidade de aceitação de uma solução de piora
                ap = math.exp(-delta / T)

                # verifica se aceita ou não uma solução
                if ap > random.random():
                    # copia a nova solução
                    self.solution = new_solution
                    # atualiza o custo
                    self.weight = new_weight
            T = T * alpha

    def get_solution(self):
        return self.solution


one_max = OneMax(500)
print(f"Solução inicial: {one_max.get_solution()}")
print("\n" * 3)
one_max.run_annealing()
print(f"Solução final: {one_max.get_solution()}")
