def dfs(n, r, c):
    return 2 * (r % 2) + (c % 2) + 4 * dfs(n - 1, r // 2, c // 2) if n != 0 else 0


n, r, c = map(int, input().split())
print(dfs(n, r, c))
