# distance hamming in Python


def hamming(string1, string2):

    len_string1, len_string2 = len(string1), len(string2)
    if len_string1 != len_string2:
        raise ValueError("Sequencias de tamanhos diferentes!")

    distancia = 0

    for i in range(len_string1):
        if string1[i] != string2[i]:
            distancia += 1
    return distancia


print(hamming("arlan", "allan")) #1
print(hamming('10011', '10100')) #3
