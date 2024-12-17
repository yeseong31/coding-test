def solution(n):
    def get_count(x):
        return bin(x)[2:].count('1')
    
    cnt = get_count(n)
    for x in range(n + 1, 1_000_001):
        if get_count(x) == cnt:
            return x
