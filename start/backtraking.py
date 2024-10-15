# backtracking algorithm in Python
# generate all subsets of a set


def generate_sub_set(subset, vector, index):
    if index == len(vector):
        print(subset)
    else:
        generate_sub_set(subset, vector, index + 1)
        subset.append(vector[index])
        generate_sub_set(subset, vector, index + 1)
        subset.pop()


s = [1, 2, 3]
generate_sub_set([], s, 0)


def sub_set_gen(subset, vector, K, N):

    if K == N:
        print("{", end="")
        for i in range(N):
            if vector[i] is True:
                print(f"{subset[i]}", end=" ")
        print("}")
    else:
        vector[K] = True
        sub_set_gen(subset, vector, K + 1, N)
        vector[K] = False
        sub_set_gen(subset, vector, K + 1, N)


s = [1, 2, 3]
sub_set_gen(s, [False] * len(s), 0, len(s))
