# Needleman-Wunsch algorithm in Python
import sys


def needleman_wunsch(str1, str2, match, mismatch, gap):
    colunas, linhas = len(str1) + 1, len(str2) + 1

    # cria a matriz de pontuacao
    matriz = [[0 for _ in range(colunas)] for _ in range(linhas)]

    # direções para construir o alinhamento
    traceback = {}

    # preenche a primeira linha e a primeira coluna
    matriz[0][0] = 0
    for i in range(1, colunas):
        matriz[0][i] = matriz[0][i - 1] + gap
        traceback[(0, i)] = (0, i - 1)
    for i in range(1, linhas):
        matriz[i][0] = matriz[i - 1][0] + gap
        traceback[(i, 0)] = (i - 1, 0)

    # função que retorna o valor máximo
    def max_valor(i, j):
        # diagonal esquerda
        valor1 = matriz[i - 1][j - 1] + (
            match if str1[j - 1] == str2[i - 1] else mismatch
        )
        valor2 = matriz[i - 1][j] + gap  # acima/topo
        valor3 = matriz[i][j - 1] + gap  # esquerda

        # calcula o valor máximo
        valor_max = max(valor1, valor2, valor3)

        # verifica o valor máximo
        if valor_max == valor1:
            traceback[(i, j)] = (i - 1, j - 1)
        elif valor_max == valor2:
            traceback[(i, j)] = (i - 1, j)
        else:
            traceback[(i, j)] = (i, j - 1)
        return valor_max

    # preenche o restante da matriz
    for i in range(1, linhas):
        for j in range(1, colunas):
            matriz[i][j] = max_valor(i, j)

    # resultados do alinhamento
    str1_result, str2_result = "", ""
    # inicia o último valor
    i, j = linhas - 1, colunas - 1

    while True:

        i_next, j_next = traceback[(i, j)]

        if (i - 1) == i_next and (j - 1) == j_next:  # diagonal
            str1_result += str1[j_next]
            str2_result += str2[i_next]
        elif (i - 1) == i_next and j == j_next:  # acima
            str1_result += "-"
            str2_result += str2[i_next]
        elif i == i_next and (j - 1) == j_next:  # esquerda
            str1_result += str1[j_next]
            str2_result += "-"
        i, j = i_next, j_next

        if not i and not j:
            break
    str1_result, str2_result = str1_result[::-1], str2_result[::-1]
    print(f"Alinhamento:\n{str1_result}\n{str2_result}")


if __name__ == "__main__":
    # obtem a quantidade de argumentos passados
    len_args = len(sys.argv)
    if len_args == 6:
        sequencia1, sequencia2 = sys.argv[1], sys.argv[2]
        match, mismatch, gap = sys.argv[3], sys.argv[4], sys.argv[5]
        needleman_wunsch(sequencia1, sequencia2, int(match), int(mismatch), int(gap))
        # print(f"{sequencia1} {sequencia2} {match}")
    else:
        print(
            "\nExecute:\n\tpython needleman_wunsch_a.py <sequencia1> <sequencia2> <match> <mismatch> <gap>\n"
        )
        print("\nExemplo:\n\tpython needleman_wunsch_a.py GCATGCU GATTACA 1 -1 -1\n")
        print("\nExemplo:\n\tpython needleman_wunsch_a.py ACTGATTCA ACGCATCA 2 -3 -2\n")


# test
# print(needleman_wunsch_b("arlan", "allan"))  # 3.0
# print(needleman_wunsch_b("10011", "10100"))  # 0.7999999999999999
# print(needleman_wunsch_b("kitten", "sitting"))  # 1.0
# print(needleman_wunsch_b("flaw", "lawn"))  # 0.8999999999999999
# print(needleman_wunsch_b("gumbo", "gambol"))  # 2.0
# print(needleman_wunsch_b("arlan", "allan", 1, -1, -1, -0.1))  # 3.0
# print(needleman_wunsch_b("10011", "10100", 1, -1, -1, -0.1))  # 0.7999999999999999
# print(needleman_wunsch_b("kitten", "sitting", 1, -1, -1, -0.1))  # 1.0
# print(needleman_wunsch_b("flaw", "lawn", 1, -1, -1, -0.1))  # 0.8999999999999999
# print(needleman_wunsch_b("gumbo", "gambol", 1, -1, -1, -0.1))  # 2.0
