# 어떤 정수의 수열
# 목표: 연속적인 며칠 동안의 온도의 합이 가장 큰 값

import sys
input = sys.stdin.readline

# 전체 날짜의 수 n, 연속적인 날짜의 수
n, k = map(int, input().split())
temperature = list(map(int, input().split()))

max_temperature = sum(temperature[:k])

check = max_temperature
p = 0

for i in temperature[k:]:
    check -= temperature[p]
    check += i
    max_temperature = max(max_temperature, check)
    p += 1

print(max_temperature)
