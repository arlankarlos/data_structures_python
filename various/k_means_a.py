# k-means algorithm in Python
# data mining: concepts and techniques
"""
    7 2 2 100 0
    1.0 1.0
    1.5 2.0
    3.0 4.0
    5.0 7.0
    3.5 5.0
    4.5 5.0
    3.5 4.5

    Cada número da primeira linha em ordem:
        7 é a quantidade de data points
        2 é a quantidade de atributos
        2 é a quantidade de clusters
        100 é a quantidade máxima de iterações
        0 indica que o data point não possui nome

"""
import random
import math


class Ponto:
    def __init__(self, id_ponto, valores):
        self.id_ponto = id_ponto
        self.valores = valores
        self.total_valores = len(valores)
        self.id_cluster = -1

    def get_id_ponto(self):
        return self.id_ponto

    def set_cluster(self, id_cluster):
        self.id_cluster = id_cluster

    def get_cluster(self):
        return self.id_cluster

    def get_valor(self, indice):
        return self.valores[indice]

    def get_total_valores(self):
        return self.total_valores

    def add_valor(self, valor):
        self.valores.append(valor)


class Cluster:
    def __init__(self, id_cluster, ponto) -> None:
        self.id_cluster = id_cluster
        self.total_valores = ponto.get_total_valores()
        self.valores_centrais = []
        self.pontos = []

        for i in range(self.total_valores):
            self.valores_centrais.append(ponto.get_valor(i))
        self.pontos.append(ponto)

    def add_ponto(self, ponto):
        self.pontos.append(ponto)

    def remove_ponto(self, id_ponto):
        total_pontos = len(self.pontos)
        for i in range(total_pontos):
            if self.pontos[i].get_id_ponto() == id_ponto:
                self.pontos.pop(i)
                return True
        return False

    def get_valor_central(self, indice):
        return self.valores_centrais[indice]

    def set_valor_central(self, indice, valor):
        self.valores_centrais[indice] = valor

    def get_ponto(self, indice):
        return self.pontos[indice]

    def get_total_pontos(self):
        return len(self.pontos)

    def get_id_cluster(self):
        return self.id_cluster


class KMeans:
    def __init__(self, K, total_pontos, total_valores, max_iteracoes):
        self.K = K
        self.total_pontos = total_pontos
        self.total_valores = total_valores
        self.max_iteracoes = max_iteracoes
        self.clusters = []

    # retorna o centro mais próximo (usa a distância euclidiana)
    def get_id_centro_proximo(self, ponto):
        soma = 0.0
        id_cluster_centro = 0

        for i in range(self.total_valores):
            soma += pow(self.clusters[0].get_valor_central(i) - ponto.get_valor(i), 2.0)

        menor_distancia = math.sqrt(soma)
        for i in range(1, self.K):
            soma = 0.0
            for j in range(self.total_valores):
                soma += pow(
                    self.clusters[i].get_valor_central(j) - ponto.get_valor(j), 2.0
                )
            distancia = math.sqrt(soma)
            if distancia < menor_distancia:
                menor_distancia = distancia
                id_cluster_centro = i
        return id_cluster_centro

    def executar(self, pontos):
        if self.K > self.total_pontos:
            print("Erro: K maior que o total de pontos")
            return

        indices_proibidos = []

        # escolhe K valores distintos para os centros do clusters
        for i in range(self.K):
            while True:
                indice_ponto = random.randint(0, self.total_pontos - 1)
                if indice_ponto not in indices_proibidos:
                    indices_proibidos.append(indice_ponto)
                    pontos[indice_ponto].set_cluster(i)
                    cluster = Cluster(i, pontos[indice_ponto])
                    self.clusters.append(cluster)
                    break

        iteracao_ = 1

        while True:
            done = True

            # associa cada ponto ao centro mais próximo
            for i in range(self.total_pontos):
                id_cluster_velho = pontos[i].get_cluster()
                id_cluster_proximo = self.get_id_centro_proximo(pontos[i])
                if id_cluster_velho != id_cluster_proximo:
                    if id_cluster_velho != -1:
                        self.clusters[id_cluster_velho].remove_ponto(
                            pontos[i].get_id_ponto()
                        )
                    pontos[i].set_cluster(id_cluster_proximo)
                    self.clusters[id_cluster_proximo].add_ponto(pontos[i])
                    done = False

            # recalcula os centros dos clusters
            for i in range(self.K):
                for j in range(self.total_valores):
                    total_pontos_cluster = self.clusters[i].get_total_pontos()
                    soma = 0.0

                    if total_pontos_cluster > 0:
                        for p in range(total_pontos_cluster):
                            soma += self.clusters[i].get_ponto(p).get_valor(j)
                        self.clusters[i].set_valor_central(
                            j, soma / total_pontos_cluster
                        )

            if done is True or iteracao_ >= self.max_iteracoes:
                print(f"Parou na iteração {iteracao_}")
                break

            iteracao_ += 1

        # mostra os elementos de cada cluster
        for i in range(self.K):
            total_pontos_cluster = self.clusters[i].get_total_pontos()
            print(f"Cluster {i+1}:", end="")
            for j in range(total_pontos_cluster):
                print(f" {self.clusters[i].get_ponto(j).get_id_ponto() +1 }", end="")
            print()


if __name__ == "__main__":
    arquivo = open("dataset1.txt")
    linhas = arquivo.readlines()
    arquivo.close()

    primeira_linha = linhas[0].split()
    numero_data_points, numero_atributos, numero_clusters, max_iteracores = [
        int(i) for i in primeira_linha
    ]

    pontos = []
    for i in range(1, numero_data_points + 1):
        atributos = linhas[i].split()
        valores = [float(i) for i in atributos]
        ponto = Ponto(i -1, valores)
        pontos.append(ponto)

    kmeans = KMeans(numero_clusters, numero_data_points, numero_atributos, max_iteracores)
    kmeans.executar(pontos)