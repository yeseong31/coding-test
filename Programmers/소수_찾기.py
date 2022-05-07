import math
from itertools import permutations


def solution(numbers):
    def prime_number(x):
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True

    cnt = 0
    check = set()
    for i in range(1, len(numbers) + 1):
        for l in list(permutations(numbers, i)):
            n = int(''.join(l))
            if n >= 2 and n not in check and prime_number(n):
                cnt += 1
                check.add(n)

    return cnt