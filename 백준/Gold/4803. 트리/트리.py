import sys
input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a, b = find_parent(parent, a), find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


t = 1
while True:
    n, m = map(int, input().rstrip().split())
    if n == 0:
        break
        
    parent = [i for i in range(n + 1)]
    cycle = set()
    
    for _ in range(m):
        a, b = map(int, input().rstrip().split())
        if find_parent(parent, a) == find_parent(parent, b):
            cycle.add(a)
        else:
            union_parent(parent, a, b)

    for i in range(1, n + 1):
        find_parent(parent, i)
    
    check = set(parent[1:])
    for c in cycle:
        p = find_parent(parent, c)
        if p in check:
            check.remove(p)
    
    if len(check) == 0:
        print(f'Case {t}: No trees.')
    elif len(check) == 1:
        print(f'Case {t}: There is one tree.')
    else:
        print(f'Case {t}: A forest of {len(check)} trees.')
    t += 1
