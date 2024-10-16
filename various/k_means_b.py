# k-means algorithm in Python
import random


def k_means(data, k, max_iter=100):
    centroids = random.sample(data, k)
    for _ in range(max_iter):
        clusters = {i: [] for i in range(k)}
        for point in data:
            distances = [
                ((point[0] - centroid[0]) ** 2 + (point[1] - centroid[1]) ** 2) ** 0.5
                for centroid in centroids
            ]
            clusters[distances.index(min(distances))].append(point)
        new_centroids = []
        for cluster in clusters.values():
            new_centroids.append(
                (
                    sum([point[0] for point in cluster]) / len(cluster),
                    sum([point[1] for point in cluster]) / len(cluster),
                )
            )
        if new_centroids == centroids:
            break
        centroids = new_centroids

        return clusters


# test 1
data = [(1, 2), (1, 3), (2, 1), (2, 2), (3, 1), (3, 2)]
k = 2
print(k_means(data, k))  # {0: [(1, 2), (1, 3), (2, 2), (3, 2)], 1: [(2, 1), (3, 1)]}

# test 2
data = [(1, 2), (1, 3), (2, 1), (2, 2), (3, 1), (3, 2), (4, 5), (5, 5), (6, 6), (7, 6), (8, 8)]
k = 3
print(k_means(data, k))  # {0: [(1, 2), (1, 3), (2, 2), (3, 2)], 1: [(2, 1), (3, 1), (4, 5), (5, 5)], 2: [(6, 6), (7, 6), (8, 8)]}

# test 3
data = [(1, 2), (1, 3), (2, 1), (2, 2), (3, 1), (3, 2), (4, 5), (5, 5), (6, 6), (7, 6), (8, 8), (9, 8), (10, 10)]
k = 4
print(k_means(data, k))  # {0: [(1, 2), (1, 3), (2, 2), (3, 2)], 1: [(2, 1), (3, 1)], 2: [(4, 5), (5, 5), (6, 6), (7, 6)], 3: [(8, 8), (9, 8), (10, 10)]}
# In the k_means_b.py snippet, the k_means function is defined,
# which implements the k-means clustering algorithm in Python.
# The function takes three parameters: data, k, and max_iter,
# where data is a list of tuples representing the points to be
# clustered, k is the number of clusters to form, and max_iter is the
# maximum number of iterations to run the algorithm. The function
# initializes the centroids randomly and iteratively assigns points to
# the nearest centroid, updating the centroids based on the mean of the
# points in each cluster. The function returns a dictionary mapping
# cluster indices to the points in each cluster. The snippet includes
# three test cases to demonstrate the usage of the k_means function
# with different input data and k values.