# Needleman-Wunsch algorithm for global alignment of two sequences in Python
# with affine gap penalties
import numpy as np


def needleman_wunsch_b(seq1, seq2, match=1, mismatch=-1, gap_open=-1, gap_extend=-0.1):
    n = len(seq1)
    m = len(seq2)
    H = np.zeros((n + 1, m + 1))
    E = np.zeros((n + 1, m + 1))
    F = np.zeros((n + 1, m + 1))

    for i in range(1, n + 1):
        H[i, 0] = gap_open + i * gap_extend
        E[i, 0] = gap_open + i * gap_extend
    for j in range(1, m + 1):
        H[0, j] = gap_open + j * gap_extend
        F[0, j] = gap_open + j * gap_extend

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match_mismatch = H[i - 1, j - 1] + (
                match if seq1[i - 1] == seq2[j - 1] else mismatch
            )
            E[i, j] = max(H[i, j - 1] + gap_open, E[i, j - 1] + gap_extend)
            F[i, j] = max(H[i - 1, j] + gap_open, F[i - 1, j] + gap_extend)
            H[i, j] = max(match_mismatch, E[i, j], F[i, j])

    return H[n, m]


# test
print(needleman_wunsch_b("arlan", "allan"))  # 3.0
print(needleman_wunsch_b("10011", "10100"))  # 0.7999999999999999
print(needleman_wunsch_b("kitten", "sitting"))  # 1.0
print(needleman_wunsch_b("flaw", "lawn"))  # 0.8999999999999999
print(needleman_wunsch_b("gumbo", "gambol"))  # 2.0
print(needleman_wunsch_b("arlan", "allan", 1, -1, -1, -0.1))  # 3.0
print(needleman_wunsch_b("10011", "10100", 1, -1, -1, -0.1))  # 0.7999999999999999
print(needleman_wunsch_b("kitten", "sitting", 1, -1, -1, -0.1))  # 1.0
print(needleman_wunsch_b("flaw", "lawn", 1, -1, -1, -0.1))  # 0.8999999999999999
print(needleman_wunsch_b("gumbo", "gambol", 1, -1, -1, -0.1))  # 2.0
