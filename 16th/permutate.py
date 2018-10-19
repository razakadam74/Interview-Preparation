from itertools import permutations

def permutation(str):
    return permutations(list(str))

list = permutation('Ghana')
for i in list:
    print(i)