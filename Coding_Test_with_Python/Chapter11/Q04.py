# 만들 수 없는 금액(314p)

n = int(input())
data = list(map(int, input().split()))
data.sort()

d = [False] * 1001

target = 1
for i in data:
    if target >= i:
        target += i
    else:
        break

print(target)
