def check(x, c):
    cnt = 0
    while x >= c:
        x //= c
        cnt += x
    return cnt


n = int(input())

print(check(n, 5))
# print(n // 5 + n // 25 + n // 125)
