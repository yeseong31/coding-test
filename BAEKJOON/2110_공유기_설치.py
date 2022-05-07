import itertools

# 집의 개수 n, 공유기의 개수 c
n, c = map(int, input().split())
houses = sorted([int(input()) for _ in range(n)])

distance = 0
for comb in list(itertools.combinations(houses, c)):
    dist = int(1e9)
    p = comb[0]
    for i in comb[1:]:
        dist = min(dist, i - p)
        p = i
    distance = max(distance, dist)

print(distance)

# 메모리 제한....
