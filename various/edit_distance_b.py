# edit distance in Python


def edit_distance(string1, string2, len_string1, len_string2):
    if len_string1 == 0:
        return len_string2
    if len_string2 == 0:
        return len_string1
    if string1[len_string1 - 1] == string2[len_string2 - 1]:
        return edit_distance(string1, string2, len_string1 - 1, len_string2 - 1)
    return 1 + min(
        edit_distance(string1, string2, len_string1, len_string2 - 1),
        edit_distance(string1, string2, len_string1 - 1, len_string2),
        edit_distance(string1, string2, len_string1 - 1, len_string2 - 1),
    )

# test
print(edit_distance("arlan", "allan", 5, 5)) #1
print(edit_distance('10011', '10100', 5, 5)) #3
print(edit_distance('kitten', 'sitting', 6, 7)) #3
print(edit_distance('flaw', 'lawn', 4, 4)) #2
print(edit_distance('gumbo', 'gambol', 5, 6)) #2