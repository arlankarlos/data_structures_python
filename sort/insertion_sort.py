# insertion sort algorithm in Python


def insertion_sort(vector):
    for i in range(1, len(vector)):
        key = vector[i]
        j = i - 1
        while j >= 0 and key < vector[j]:
            vector[j + 1] = vector[j]
            j -= 1
        vector[j + 1] = key
    return vector


vector = [10, 40, 5, 15, 30, 70, 20]
print(insertion_sort(vector))