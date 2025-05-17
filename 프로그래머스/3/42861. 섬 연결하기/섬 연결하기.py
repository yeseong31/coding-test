from heapq import heappush, heappop


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


def solution(n, costs):
    answer = 0
    q = []
    
    for a, b, c in costs:
        heappush(q, (c, a, b))
        
    parent = list(range(n))
    
    while q:
        c, a, b = heappop(q)
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += c
    
    return answer