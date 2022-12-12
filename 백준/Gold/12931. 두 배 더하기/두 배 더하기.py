n = int(input())
b = list(map(int, input().split()))
answer = 0

while True:
    chk = _sum = 0
    for i in range(len(b)):
        if b[i] % 2 == 1:
            chk += 1
            b[i] -= 1
        _sum += b[i]
        b[i] //= 2
    answer += chk
    if _sum == 0:
        break
    answer += 1
print(answer)