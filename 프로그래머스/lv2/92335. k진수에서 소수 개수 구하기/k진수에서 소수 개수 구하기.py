def is_prime_number(n):
    if n < 2:
        return 0
    for i in range(3, int(n ** 0.5) + 1):
        if n % i == 0:
            return 0
    return 1


def change(n, k):
    result = []
    while n > 0:
        div, mod = divmod(n, k)
        result.append(str(mod))
        n = div
    return ''.join(result[::-1])


def solution(n, k):
    return sum(1 for n in change(n, k).split('0') if n != '' and is_prime_number(int(n)))