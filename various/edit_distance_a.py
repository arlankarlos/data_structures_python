# edit distance in Python


def edit_distance(str1, str2, len_str1, len_str2):
    if len_str1 == 0:
        return len_str2
    if len_str2 == 0:
        return len_str1

    distancia = 0

    if str1[len_str1 - 1] != str2[len_str2 - 1]:
        distancia = 1

    return min(
        edit_distance(str1, str2, len_str1 - 1, len_str2) + 1,
        edit_distance(str1, str2, len_str1, len_str2 - 1) + 1,
        edit_distance(str1, str2, len_str1 - 1, len_str2 - 1) + distancia,
    )


# test
print(edit_distance("arlan", "allan", 5, 5)) #1
print(edit_distance('10011', '10100', 5, 5)) #3
print(edit_distance('kitten', 'sitting', 6, 7)) #3
print(edit_distance('flaw', 'lawn', 4, 4)) #2
print(edit_distance('gumbo', 'gambol', 5, 6)) #2