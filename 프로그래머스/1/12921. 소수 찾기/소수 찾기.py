def prime_number(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def solution(n):
    return sum(prime_number(i) for i in range(2, n + 1))
