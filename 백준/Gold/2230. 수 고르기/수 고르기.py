import sys

input = sys.stdin.readline

n, m = map(int, input().split())
A = sorted([int(input()) for _ in range(n)])

answer = sys.maxsize
left = right = 0
while left < n and right < n:
    target = A[right] - A[left]
    if target == m:
        answer = m
        break
    elif target < m:
        right += 1
    else:
        left += 1
        answer = min(answer, target)
print(answer)