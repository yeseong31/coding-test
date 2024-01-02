def solution(s, n):
    answer = []
    
    for c in s:
        if c == ' ':
            answer.append(' ')
            continue
        
        offset = ord('a') if c.islower() else ord('A')
        position = (ord(c) - offset + n) % 26
        answer.append(chr(position + offset))
                
    return ''.join(answer)
