def solution(n):
    answer = 0

    s = ''
    while n > 0:
        div, mod = divmod(n, 3)
        s += str(mod)
        n = div

    return int(s, 3)