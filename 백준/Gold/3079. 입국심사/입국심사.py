import sys
input = sys.stdin.readline

n, m = map(int, input().split())
times = [int(input()) for _ in range(n)]

answer = 0
left, right = 0, max(times) * m

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    check = False
    for t in times:
        cnt += mid // t
        if cnt >= m:
            check = True
            
    if check:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)