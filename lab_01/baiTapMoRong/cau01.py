from itertools import permutations

data = [1, 2, 3]
perms_full = permutations(data)
print("Full permutations:")
for p in perms_full:
    print(p)