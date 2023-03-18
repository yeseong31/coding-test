from itertools import permutations


def solution(numbers):
    def is_prime_number(n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    answer = set()
    
    for i in range(1, len(numbers) + 1):
        for perm in set(permutations(numbers, i)):
            target = int(''.join(perm))
            if is_prime_number(target):
                answer.add(target)

    return len(answer)
