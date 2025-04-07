n = int(input())
lst = sorted(list(map(int, input().split())))
x = int(input())

cnt = 0
left, right = 0, n - 1
while left < right:
    target = lst[left] + lst[right]
    if x == target:
        cnt += 1
        left += 1
        right -= 1
    elif x < target:
        right -= 1
    else:
        left += 1

print(cnt)
