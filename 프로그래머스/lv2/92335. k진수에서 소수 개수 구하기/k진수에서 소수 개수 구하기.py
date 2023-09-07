def solution(n, k):
    def is_prime_number(x):
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return not x < 2
    
    def change_digit(x):
        result = []
        while x != 0:
            x, mod = divmod(x, k)
            result.append(str(mod))
        return ''.join(result[::-1])
    
    answer = 0
    for target in change_digit(n).split('0'):
        if not target.isdigit():
            continue
        if is_prime_number(int(target)):
            answer += 1
    return answer