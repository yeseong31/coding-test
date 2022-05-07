from itertools import combinations


def solution(nums):
    def is_prime_number(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    answer = 0
    for n in list(combinations(nums, 3)):
        if is_prime_number(sum(n)):
            answer += 1

    return answer