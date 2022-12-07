def solution(s):
    answer = 0
    l, r, c = 0, 1, 1  # 왼쪽, 오른쪽, 카운트
    
    while r < len(s):
        c += 1 if s[l] == s[r] else -1
        r += 1
        if c != 0:
            continue
        l, r, c = r, r + 1, 1
        answer += 1
        
    if l < len(s):
        answer += 1
    return answer