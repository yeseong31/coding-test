n, s = map(int, input().split())
lst = list(map(int, input().split()))

answer = 100001
l = r = 0
value = lst[0]

while True:
    if value >= s:
        answer = min(answer, r - l + 1)
        value -= lst[l]
        l += 1
    else:
        r += 1
        if r == n:
            break
        value += lst[r]

if answer == 100001:
    print(0)
else:
    print(answer)