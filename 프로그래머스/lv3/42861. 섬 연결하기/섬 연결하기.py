def find_parent(parent, x):
    if parent[x] == x:
        return x
    return find_parent(parent, parent[x])


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

        
def solution(n, costs):
    answer = 0
    parent = [0] * (n + 1)
    
    for i in range(n + 1):
        parent[i] = i
        
    costs.sort(key=lambda x: x[2])
    
    for a, b, c in costs:
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += c
    
    return answer