def solution(s, skip, index):
    answer = ''
    
    for c in s:
        count = 0
        
        while count < index:
            c = chr(ord(c) + 1)
            if c > 'z':
                c = 'a'
            if c not in skip:
                count += 1
                
        answer += c
        
    return answer