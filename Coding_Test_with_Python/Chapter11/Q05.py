# 볼링공 고르기(315p)

from itertools import combinations

# 볼링공의 개수 n, 공의 최대 무게 m
n, m = map(int, input().split())
data = list(map(int, input().split()))

result = 0
for a, b in list(combinations(data, 2)):
    if a != b:
        result += 1

print(result)
