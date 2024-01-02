from itertools import combinations


def solution(line):
    points = set()
    min_x = min_y = int(1e15)
    max_x = max_y = -int(1e15)
    
    for lineA, lineB in combinations(line, 2):
        (a, b, e), (c, d, f) = lineA, lineB

        if a * d == b * c:
            continue
        
        x = (b * f - e * d) / (a * d - b * c)
        y = (e * c - a * f) / (a * d - b * c)
        
        if x == int(x) and y == int(y):
            x, y = int(x), int(y)
            min_x, min_y = min(x, min_x), min(y, min_y)
            max_x, max_y = max(x, max_x), max(y, max_y)
            points.add((x, y))
    
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    board = [['.'] * width for _ in range(height)]
    
    for x, y in points:
        board[max_y - y][x - min_x] = '*'
        
    return [''.join(row) for row in board]
