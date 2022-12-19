def solution(s):
    answer = len(s)
    
    for n in range(1, len(s) // 2 + 1):
        i = 0
        prev = ''
        count = 1
        result = ''
        
        while i < len(s):
            target = s[i:i + n]
            if target == prev:
                count += 1
            elif prev != '':
                result += f'{count}{prev}' if count != 1 else prev
                count = 1
            prev = target
            i += n
            
        result += f'{count}{prev}' if count != 1 else prev
        answer = min(answer, len(result))
        
    return answer