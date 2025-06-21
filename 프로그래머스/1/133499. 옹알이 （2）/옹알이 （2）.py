def solution(babbling):
    check = ['aya', 'ye', 'woo', 'ma']
    answer = 0
    
    for v in babbling:
        for c in check:
            if c * 2 not in v:
                v = v.replace(c, ' ')
        
        if not v.split():
            answer += 1
        
    return answer