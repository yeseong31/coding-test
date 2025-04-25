from itertools import combinations

INF = int(1e12)


def solution(line):
    points = set()
    
    min_x, min_y = INF, INF
    max_x, max_y = -INF, -INF
    
    for (a, b, e), (c, d, f) in combinations(line, 2):
        if a * d == b * c:
            continue
        
        x = ((b * f) - (e * d)) / ((a * d) - (b * c))
        y = ((e * c) - (a * f)) / ((a * d) - (b * c))
        
        if x != int(x) or y != int(y):
            continue
            
        x, y = int(x), int(y)
        min_x, min_y = min(x, min_x), min(y, min_y)
        max_x, max_y = max(x, max_x), max(y, max_y)
        points.add((x, y))
                       
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    answer = [['.'] * width for _ in range(height)]

    for x, y in points:
        col = x - min_x
        row = max_y - y
        answer[row][col] = '*'
    
    return [''.join(row) for row in answer]
