import itertools

n, m = map(int, input().split())

for lst in list(itertools.permutations(list(range(1, n + 1)), m)):
    print(*lst)