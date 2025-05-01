from itertools import permutations


def solution(numbers):
    result = set()
    
    for i in range(1, len(numbers) + 1):
        for x in permutations(numbers, i):
            number = int(''.join(x))
            result.add(number)
    
    return sum(is_prime_number(x) for x in result)


def is_prime_number(x):
    if x <= 1:
        return False
    
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
        
    return True
