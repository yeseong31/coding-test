import math
import sys
input = sys.stdin.readline

n, l = map(int, input().split())
answer = p = 0

for s, e in sorted([[int(x) for x in input().split()] for _ in range(n)]):
    s = max(s, p)
    d = math.ceil((e - s) / l)
    answer += d
    p = s + d * l
print(answer)