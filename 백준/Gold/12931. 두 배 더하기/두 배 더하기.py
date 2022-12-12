n = int(input())
b = list(map(int, input().split()))
ans = 0

while True:
    c = s = 0
    for i in range(n):
        if b[i] % 2 == 1:
            c += 1
            b[i] -= 1
        b[i] //= 2
        s += b[i]
    ans += c + 1
    if s == 0:
        print(ans - 1)
        break