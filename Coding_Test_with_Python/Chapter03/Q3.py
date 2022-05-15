
# 예제 3-3 숫자 카드 게임(96p)

n, m = map(int, input().split())
res = 0

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

for d in data:
    res = max(res, min(d))

print(res)