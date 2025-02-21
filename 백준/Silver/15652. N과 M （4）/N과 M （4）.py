import itertools

n, m = map(int, input().split())

for lst in list(itertools.combinations_with_replacement(list(range(1, n + 1)), m)):
    print(*lst)