"""
치킨 배달 (332p)
"""


import itertools

# 도시 크기 n, 폐업시키지 않을 치킨 집 개수 m
n, m = map(int, input().split())
house, chicken = [], []
for i in range(n):
    row = list(map(int, input().split()))
    for j, r in enumerate(row):
        if r == 1:
            house.append((i, j))
        elif r == 2:
            chicken.append((i, j))

# m개의 치킨집을 선택하여 도시의 치킨 거리의 최솟값을 계산
result = 10000
for chickens in list(itertools.combinations(chicken, m)):
    dist = 0
    # 각각의 집에 대해 치킨 거리의 최솟값을 계산
    for x, y in house:
        d = 100
        for a, b in chickens:
            d = min(d, abs(x - a) + abs(y - b))
        dist += d
    result = min(result, dist)

print(result)
