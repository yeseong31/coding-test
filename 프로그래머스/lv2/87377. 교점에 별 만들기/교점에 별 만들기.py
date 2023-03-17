from itertools import combinations

def solution(line):
    points = []
    x_max = y_max = -int(1e15)
    x_min = y_min = int(1e15)
    
    for (a, b, e), (c, d, f) in list(combinations(line, 2)):
        if a * d - b * c == 0:
            continue
        x = (b * f - e * d) / (a * d - b * c)
        y = (e * c - a * f) / (a * d - b * c)
        if x.is_integer() and y.is_integer():
            x, y = int(x), int(y)
            points.append((x, y))
            x_max, y_max = max(x_max, x), max(y_max, y)
            x_min, y_min = min(x_min, x), min(y_min, y)
        
    board = [['.'] * (x_max - x_min + 1) for _ in range(y_max - y_min + 1)]
    for px, py in points:
        board[py - y_min][px - x_min] = '*'
        
    return [''.join(b) for b in board[::-1]]