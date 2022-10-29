def check(x, c):
    cnt = 0
    while x >= c:
        x //= c
        cnt += x
    return cnt


n, m = map(int, input().split())
check_2 = check(n, 2) - check(m, 2) - check(n - m, 2)
check_5 = check(n, 5) - check(m, 5) - check(n - m, 5)
print(min(check_2, check_5))

