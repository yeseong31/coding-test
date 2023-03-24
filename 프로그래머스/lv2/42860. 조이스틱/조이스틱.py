def solution(name):
    count = 0
    n = len(name)
    _min = n - 1
    
    for i, v in enumerate(name):
        # 'A'를 문자 v로 바꾸고
        count += min(ord(v) - ord('A'), ord('Z') - ord(v) + 1)
        # (왼쪽->오른쪽) 방향으로 'A'가 아닌 문자의 위치를 구하고
        idx = i + 1
        while idx < n and name[idx] == 'A':
            idx += 1
        # 최소 거리를 계산하여 min_move 갱신
        _min = min(_min, 2 * i + (n - idx), 2 * (n - idx) + i)
    
    # 문자 변환 + 이동 거리 반환
    return count + _min
