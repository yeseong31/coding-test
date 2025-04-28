from collections import deque


def solution(s):
    answer = len(s)
    
    for n in range(1, len(s) // 2 + 1):
        answer = min(answer, compress(s, n))
    
    return answer


def compress(s, n):
    q = deque()
    index = 0
    
    while index < len(s):
        q.append(s[index:index+n])
        index += n
    
    result = []
    prev = q.popleft()
    count = 1
    
    while q:
        cur = q.popleft()
        
        if prev == cur:
            count += 1
            continue
        
        result.append(prev if count == 1 else f'{count}{prev}')
        prev = cur
        count = 1

    result.append(prev if count == 1 else f'{count}{prev}')
    return len(''.join(result))
