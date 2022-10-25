# 개똥벌레
import sys

input = sys.stdin.readline
n, h = map(int, input().split())

odd = [0] * (h + 1)
even = [0] * (h + 1)

for i in range(n):
    x = int(input())
    if i % 2 == 0:
        even[x] += 1
    else:
        odd[x] += 1

for i in range(h - 2, 0, -1):
    odd[i] += odd[i + 1]
    even[i] += even[i + 1]

min_value = 500001
count = 0
for i in range(1, h + 1):
    target = odd[i] + even[h - i + 1]
    if min_value > target:
        min_value = target
        count = 1
    elif min_value == target:
        count += 1

print(min_value, count)
