# pattern matching algorithm with brute force in Python


def brute_force(texto, padrao):
    len_texto, len_padrao = len(texto), len(padrao)

    for i in range(len_texto - len_padrao + 1):

        j = 0
        while j < len_padrao and texto[i + j] == padrao[j]:
            j += 1
        if j == len_padrao:
            print(f"Padrão encontrado no índice {i}")
    return -1



# test
text = "AABAACAADAABAAABAA"
pattern = "AABA"
brute_force(text, pattern)
# Pattern found at index 0
# Pattern found at index 9
# Pattern found at index 13

# test
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
brute_force(text, pattern)
# Pattern found at index 10

# test
texto = "python é uma excelente linguagem, pois python é fácil de aprender"
padrao = "python"
brute_force(texto, padrao)
# Padrão encontrado no índice 0
# Padrão encontrado no índice 39
