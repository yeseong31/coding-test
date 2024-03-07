def prime_lst(n):
    d = [True] * n
    for i in range(2, int(n ** 0.5) + 1):
        if d[i]:
            for j in range(i * 2, n, i):
                d[j] = False
    return [i for i in range(2, n) if d[i]]

def goldbach(n):
    lst = prime_lst(n)
    index = max([i for i in range(len(lst)) if lst[i] <= n // 2])
    for i in range(index, -1, -1):
        for j in range(i, len(lst)):
            if lst[i] + lst[j] == n:
                return [lst[i], lst[j]]

for _ in range(int(input())):
    g = goldbach(int(input()))
    print(g[0], g[1])