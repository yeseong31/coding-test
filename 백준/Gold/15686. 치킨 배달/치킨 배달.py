from itertools import combinations

n, m = map(int, input().split())
houses, chickens = [], []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            houses.append((i, j))
        elif row[j] == 2:
            chickens.append((i, j))

answer = 4 * n ** 2
for comb in list(combinations(chickens, m)):
    answer = min(answer, sum(min(abs(hx - cx) + abs(hy - cy) for cx, cy in comb) for hx, hy in houses))
print(answer)