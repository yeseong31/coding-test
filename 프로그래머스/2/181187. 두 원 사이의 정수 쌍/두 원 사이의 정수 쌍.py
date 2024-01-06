def calculate(r, w):
    return (r ** 2 - w ** 2) ** 0.5


def solution(r1, r2):
    answer = 0
    
    for w in range(1, r2):
        h1, h2 = calculate(r1, w), calculate(r2, w)
        
        if w >= r1:
            answer += int(h2) + 1
            continue
        
        answer += int(h2) - int(h1)
        
        if h1 == int(h1):
            answer += 1
        
    return 4 * (answer + 1)
