def solution(n):
    a = b = 1
    
    for x in range(2, n + 1):
        a, b = b, a + b
    
    return a % 1_234_567