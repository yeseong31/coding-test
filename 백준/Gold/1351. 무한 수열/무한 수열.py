from collections import defaultdict


def dfs(x, a, b):
    if x == 0:
        return 1
    if not visited[x]:
        visited[x] = dfs(x // a, a, b) + dfs(x // b, a, b)
    return visited[x]


n, p, q = map(int, input().split())
visited = defaultdict(int)
print(dfs(n, p, q))