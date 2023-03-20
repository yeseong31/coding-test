def check(x, n):
    while n >= 1:
        div, mod = divmod(x, 5)
        if div == 1:
            return '11011'[mod]
        if mod == 2:
            return '0'
        x = div
        n -= 1
    return '1'


def solution(n, l, r):
    return [check(x, n) for x in range(l - 1, r)].count('1')