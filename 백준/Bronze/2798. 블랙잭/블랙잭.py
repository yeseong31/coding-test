from itertools import combinations 

n, m = map(int, input().split())
data = list(combinations(list(map(int, input().split())), 3))

res = 0
for d in data:
    comp = sum(d[:])
    if comp <= m:
        res = max(res, comp)
print(res)  