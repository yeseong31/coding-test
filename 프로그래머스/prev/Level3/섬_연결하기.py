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

    parent = list(range(n))
    answer = 0

    for cost, a, b in sorted([(w, u, v) for u, v, w in costs], key=lambda x: x[0]):
        if find_parent(parent, a) != find_parent(parent, b):
            make_union(parent, a, b)
            answer += cost

    return answer


n, costs = 4, [[0, 1, 16], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]
print(solution(n, costs))
