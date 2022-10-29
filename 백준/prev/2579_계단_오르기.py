import sys
input = sys.stdin.readline

# 계단의 개수 n
n = int(input())
# 계단
stairs = [0] * 301
# dp 테이블
d = [0] * 301

for i in range(n):
    stairs[i] = int(input())

d[0] = stairs[0]
d[1] = stairs[0] + stairs[1]
d[2] = max(stairs[0], stairs[1]) + stairs[2]

for i in range(3, n):
    d[i] = max(d[i - 3] + stairs[i - 1], d[i - 2]) + stairs[i]
print(d[n - 1])
