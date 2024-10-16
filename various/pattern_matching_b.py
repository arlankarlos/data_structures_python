# pattern matching algorithm with brute force in Python


def brute_force(text, pattern):
    len_text = len(text)
    len_pattern = len(pattern)
    for i in range(len_text - len_pattern + 1):
        j = 0
        while j < len_pattern and text[i + j] == pattern[j]:
            j += 1
        if j == len_pattern:
            print(f"Pattern found at index {i}")


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

