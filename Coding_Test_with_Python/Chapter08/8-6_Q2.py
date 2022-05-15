# 실전 문제 - 개미 전사(220p)

# 최소한 한 칸 이상 떨어진 식량창고를 약탈

# 식량창고의 개수 N
n = int(input())
# 식량창고에 저장된 식량의 개수 K
k = list(map(int, input().split()))

d = [0] * 100
d[0] = k[0]
d[1] = max(k[0], k[1])

for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + k[i])

print(d[n - 1])
