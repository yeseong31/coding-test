def solution(n, s):
    if n > s:
        return [-1]
    
    answer = [s // n] * n
    
    for _ in range(s % n):
        n -= 1
        answer[n] += 1
    
    return answer
