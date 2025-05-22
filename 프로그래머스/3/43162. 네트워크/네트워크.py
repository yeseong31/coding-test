def find_parent(parents, x):
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]

def union_parent(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

def solution(n, computers):
    parents = list(range(n))
    
    for i in range(n):
        for j in range(i):
            if i != j and computers[i][j] == 1:
                union_parent(parents, i, j)
    
    root_set = set(find_parent(parents, i) for i in range(n))
    return len(root_set)
