import sys

input = sys.stdin.readline

answer = 0
target = [sorted(tuple(map(int, input().split()))) for _ in range(int(input()))]
lines = sorted(target, reverse=True)
l, r = lines.pop()

while lines:
    a, b = lines.pop()
    if a <= r < b:
        r = b
    elif r < a:
        answer += r - l
        l, r = a, b

print(answer + (r - l))