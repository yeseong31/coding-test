from itertools import permutations


def solution(numbers):
    def is_prime_num(x):
        if x <= 1:
            return False
        
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        
        return True
    
    perm = [list(permutations(numbers, i)) for i in range(1, len(numbers) + 1)]
    return sum(is_prime_num(n) for n in set(int(''.join(y)) for x in perm for y in x))
