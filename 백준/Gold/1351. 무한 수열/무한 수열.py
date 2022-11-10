from collections import defaultdict


def dfs(x):
    if not visited[x]:
        visited[x] = dfs(x // p) + dfs(x // q)
    return visited[x]


n, p, q = map(int, input().split())
visited = defaultdict(int)
visited[0] = 1
print(dfs(n))