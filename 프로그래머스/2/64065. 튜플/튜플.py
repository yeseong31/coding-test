def solution(s):
    answer = list()
    checked = set()
    
    s = sorted(s[2:-2].split('},{'), key=len)
    
    for target in s:
        for v in target.split(','):
            if v not in checked:
                answer.append(int(v))
                checked.add(v)
    
    return answer
    