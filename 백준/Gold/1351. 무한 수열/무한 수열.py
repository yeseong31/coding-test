import sys
from collections import defaultdict

n, p, q = map(int, sys.stdin.readline().split())
a = defaultdict(int)
a[0] = 1


def dfs(x):
    if a[x] != 0:
        return a[x]

    a[x] = dfs(x // p) + dfs(x // q)
    return a[x]


print(dfs(n))
