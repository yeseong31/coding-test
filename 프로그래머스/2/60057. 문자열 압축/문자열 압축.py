def compress(s: str, token: int) -> int:
    result = []
    prev = s[:token]
    count = 1
    
    for start in range(token, len(s), token):
        end = min(len(s), start + token)
        target = s[start:end]
        
        if prev == target:
            count += 1
            continue
        
        if count > 1:
            result.append(str(count))
        
        result.append(prev)
        prev = target
        count = 1
    
    if count > 1:
        result.append(str(count))

    result.append(prev)
    return len(''.join(result))
        


def solution(s):
    answer = len(s)
    
    for token in range(1, len(s) // 2 + 1):
        answer = min(answer, compress(s, token))
    
    return answer
