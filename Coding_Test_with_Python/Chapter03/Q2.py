
# 예제 3-2 큰 수의 법칙(92p)

n, m, k = map(int, input().split())
lst = list(map(int, input().split()))
res = 0

lst.sort()
first = lst[n - 1]
second = lst[n - 2]

res += (first * k + second) * (m // (k + 1))
res += k * (m % (k + 1))

print(res)
