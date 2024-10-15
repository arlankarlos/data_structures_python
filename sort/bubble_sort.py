# bubble sort algorithm in Python
def bubble_sort_a(vector):
    length = len(vector)

    for i in range(length):
        swapped = False
        for j in range(0, length - i - 1):
            if vector[j] > vector[j + 1]:
                vector[j], vector[j + 1] = vector[j + 1], vector[j]
                swapped = True
        if not swapped:
            break
    return vector


def bubble_sort_b(vector):
    length = len(vector)
    ordered = length - 1

    while ordered >= 1:
        swapped = False
        for i in range(ordered):
            if vector[i] > vector[i + 1]:
                vector[i], vector[i + 1] = vector[i + 1], vector[i]
                swapped = True
        if not swapped:
            break
        ordered -= 1


vector = [10, 40, 5, 15, 30, 70, 20]
bubble_sort_a(vector)
print(vector)


vector = [10, 40, 5, 15, 30, 70, 20]
bubble_sort_b(vector)
print(vector)
