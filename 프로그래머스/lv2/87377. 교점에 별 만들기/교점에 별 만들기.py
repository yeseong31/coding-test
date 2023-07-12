from itertools import combinations


def solution(line):
    answer = []
    
    # 교점 리스트 구하기
    points = []
    for (a, b, e), (c, d, f) in combinations(line, 2):
        # 두 직선이 평행하거나 일치하면 확인하지 않음
        if (a * d - b * c) == 0:
            continue
        # 교점 공식 활용
        x = (b * f - e * d) / (a * d - b * c)
        y = (e * c - a * f) / (a * d - b * c)
        # 교점 (x, y)가 정수 칸에 있는지 확인
        if x == int(x) and y == int(y):
            points.append((int(x), int(y)))
    
    # 최소 사각형 크기 알아내기
    ldx = ldy = int(1e15)
    rux = ruy = -int(1e15)
    for x, y in points:
        ldx, ldy, rux, ruy = min(ldx, x), min(ldy, y), max(rux, x), max(ruy, y)
    
    # 최소 사각형에 교점 그리기
    board = [['.'] * (rux - ldx + 1) for _ in range(ruy - ldy + 1)]
    for x, y in points:
        nx = x + abs(ldx) if ldx < 0 else x - ldx
        ny = y + abs(ldy) if ldy < 0 else y - ldy
        board[ny][nx] = '*'
    
    # 문자 합치기
    for b in board:
        answer.append(''.join(b))
    
    return answer[::-1]
