def check(x, n, target):
    for i in range(n, 0, -1):
        x, mod = divmod(x, 5)
        if mod == 2:
            return False
        if x == 1:
            return target[mod]
    return True


def solution(n, l, r):
    target = 1, 1, 0, 1, 1
    return sum(check(x, n, target) for x in range(l - 1, r))