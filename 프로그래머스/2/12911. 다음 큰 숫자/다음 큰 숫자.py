def solution(n):
    cnt = bin(n)[2:].count('1')
    
    for x in range(n + 1, 1_000_001):
        if bin(x)[2:].count('1') == cnt:
            return x