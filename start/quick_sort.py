# quick sort algorithm in Python
def quick_sort_a(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort_a(less) + [pivot] + quick_sort_a(greater)


# test
arr = [10, 40, 5, 15, 30, 70, 20]
print(quick_sort_a(arr))  # [5, 10, 15, 20, 30, 40, 70]


def particiona(vetor, inicio, fim):
    # o pivô é o elemento inicial
    pivo = inicio

    for i in range(inicio + 1, fim + 1):
        if vetor[i] <= vetor[inicio]:
            pivo += 1
            vetor[i], vetor[pivo] = vetor[pivo], vetor[i]
    vetor[pivo], vetor[inicio] = vetor[inicio], vetor[pivo]
    return pivo


# passa a lista, o início e o fim da lista
def quick_sort_b(vetor, inicio, fim):
    """
    Se o fim for maior que o início, então
    eu calculo a posição do pivô utilizando
    a função particiona
    """
    if inicio < fim:
        pivo = particiona(vetor, inicio, fim)
        """
            Tendo o pivô, eu chamo a função duas
            vezes para cada partição, a primeira
            dos elementos que estão antes do pivô
            e a segunda é a dos elementos que estão
            depois do pivô
        """
        quick_sort_b(vetor, inicio, pivo - 1)
        quick_sort_b(vetor, pivo + 1, fim)


# test
arr = [10, 40, 5, 15, 30, 70, 20]
quick_sort_b(arr, 0, len(arr) - 1)
print(arr)  # [5, 10, 15, 20, 30, 40, 70]
