def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(n, computers):
    parent = list(range(n))
    
    for i in range(1, n):
        for j in range(i):
            if i == j or computers[i][j] == 0:
                continue
            union_parent(parent, i, j)
    
    for i in range(n):
        parent[i] = find_parent(parent, i)
    
    return len(set(parent))