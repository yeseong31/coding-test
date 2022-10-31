def solution(n, k):
    def change(a, b):
        res = []
        while a != 0:
            div, mod = divmod(a, b)
            res.append(str(mod))
            a = div
        return ''.join(res[::-1])

    def is_prime_number(c):
        if c == 1:
            return False
        for i in range(2, int(c ** 0.5) + 1):
            if c % i == 0:
                return False
        return True

    cnt = 0
    # n을 k진법으로 변환
    target = change(n, k)
    # '0' 기준으로 split하여 소수 판별
    for t in target.split('0'):
        if t == '':
            continue
        if is_prime_number(int(t)):
            cnt += 1
    return cnt


print(solution(437674, 3))
