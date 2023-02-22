import sys

input = sys.stdin.readline


def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
m = int(input())

parent = list(range(n + 1))
edges = []
answer = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

for edge in sorted(edges):
    c, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        answer += c

print(answer)