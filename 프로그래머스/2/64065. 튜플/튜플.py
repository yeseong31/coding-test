def solution(s):
    answer = dict()
    s = sorted(s[2:-2].split("},{"), key=len)
    
    for target in s:
        for v in target.split(','):
            if v not in answer:
                answer[v] = 1
    
    return list(map(int, answer))
    