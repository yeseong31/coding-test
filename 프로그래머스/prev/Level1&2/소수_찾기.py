def solution(n):
    def prime_number(x):
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    cnt = 0
    for i in range(1, n + 1):
        if prime_number(i):
            cnt += 1

    return cnt