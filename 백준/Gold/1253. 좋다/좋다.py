import sys
input = sys.stdin.readline

answer = 0
n = int(input())
nums = sorted(map(int, input().split()))

for i in range(n):
    lst = nums[:i] + nums[i + 1:]
    target = nums[i]
    l, r = 0, n - 2
    while l < r:
        v = lst[l] + lst[r]
        if v == target:
            answer += 1
            break
        if v < target:
            l += 1
        else:
            r -= 1
print(answer)