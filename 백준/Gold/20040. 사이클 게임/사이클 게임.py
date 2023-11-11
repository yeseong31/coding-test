import sys
input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = list(range(n + 1))
answer = 0


def solve():
    for i in range(m):
        x, y = map(int, input().split())
        if find_parent(parent, x) == find_parent(parent, y):
            print(i + 1)
            return
        
        union_parent(parent, x, y)
    
    print(0)


solve()
