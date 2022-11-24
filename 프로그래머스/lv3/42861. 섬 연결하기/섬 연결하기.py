def solution(n, costs):
    def find_parent(parent, x):
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]
    
    def make_union(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
    
    answer = 0
    parent = list(range(n))
    
    for c, a, b in sorted([(c, a, b) for a, b, c in costs], key=lambda x: x[0]):
        if find_parent(parent, a) != find_parent(parent, b):
            make_union(parent, a, b)
            answer += c
    
    return answer