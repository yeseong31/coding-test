n = int(input())
s = sorted(list(map(int, input().split())))

l, r = 0, n - 1
answer = []
diff = int(2e9) + 1

while l < r:
    target = s[l] + s[r]
    if abs(target) < diff:
        answer = [s[l], s[r]]
        diff = abs(target)
    if target < 0:
        l += 1
    else:
        r -= 1

print(*answer)