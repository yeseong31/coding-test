import itertools


def solution(line):
    # 방정식 계산
    def calcul(l1, l2, p):
        a, b, e = l1
        c, d, f = l2
        # 분모가 0인 경우는 확인하지 않음
        if not a * d == b * c:
            x = (b * f - e * d) / (a * d - b * c)
            y = (e * c - a * f) / (a * d - b * c)
            if x == int(x) and y == int(y):
                p.add((int(x), int(y)))

    points = set()
    # 교점 정보 확인
    for comb in list(itertools.combinations(line, 2)):
        calcul(comb[0], comb[1], points)
    # 좌표 영역 구성
    point_x, point_y = [v[0] for v in points], [v[1] for v in points]
    min_x, min_y, max_x, max_y = min(point_x), min(point_y), max(point_x), max(point_y)
    board = [['.'] * (max_x - min_x + 1) for _ in range(max_y - min_y + 1)]
    # 좌표 영역에 교점 표시
    for x, y in points:
        board[max_y - y][x - min_x] = '*'
    return [''.join(b) for b in board]


line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
print(solution(line))

line = [[0, 1, -1], [1, 0, -1], [1, 0, 1]]
print(solution(line))

line = [[1, -1, 0], [2, -1, 0]]
print(solution(line))

line = [[1, -1, 0], [2, -1, 0], [4, -1, 0]]
print(solution(line))

# 직선의 교점 중 '정수' 좌표에 대해 별을 그리고자 함
# 좌표공간의 크기는 최소로 하여 결과 반환
