def is_prime_number(n):
    if n < 2:
        return False
    
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    
    return True


def make_combinations(target, numbers, used, combinations):
    if is_prime_number(target):
        combinations.add(target)
    
    for index, number in enumerate(numbers):
        if used[index]:
            continue
        
        next_target = target * 10 + number
        
        used[index] = True
        make_combinations(next_target, numbers, used, combinations)
        used[index] = False


def solution(numbers):
    combinations = set()
    used = [False] * len(numbers)
    numbers = [int(n) for n in numbers]
    
    make_combinations(0, numbers, used, combinations)
    
    return len(combinations)
