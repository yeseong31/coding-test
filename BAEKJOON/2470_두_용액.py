# 용액: 산성(양수), 알칼리(음수)
# 두 용액을 혼합하여 특성값이 0에 가까운 용액을 만들고자 함

n = int(input())
s = sorted(list(map(int, input().split())))

l, r = 0, n - 1
answer = []
diff = int(2e9) + 1

while l < r:
    # 구한 값이 0에 더 가까울 경우
    target = s[l] + s[r]
    if abs(target) < diff:
        answer = [s[l], s[r]]
        diff = abs(target)
    if target < 0:
        l += 1
    else:
        r -= 1

print(*answer)
