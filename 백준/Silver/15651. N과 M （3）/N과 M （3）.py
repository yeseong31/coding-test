import itertools

n, m = map(int, input().split())

for lst in list(itertools.product(list(range(1, n + 1)), repeat=m)):
    print(*lst)