from collections import defaultdict, Counter
from itertools import zip_longest


def move_point(x, y, nx, ny):
    result = []
    
    step = 1 if x <= nx else -1
    for x in range(x + step, nx + step, step):
        result.append((x, y))
        
    step = 1 if y <= ny else -1
    for y in range(y + step, ny + step, step):
        result.append((x, y))
        
    return result


def get_footprints(points, via_routes):
    result = [tuple(points[via_routes[0] - 1])]
    
    for index in range(1, len(via_routes)):
        x, y = points[via_routes[index - 1] - 1]
        nx, ny = points[via_routes[index] - 1]
        
        result.extend(move_point(x, y, nx, ny))
    
    return result


def solution(points, routes):
    answer = 0
    
    footprints = [get_footprints(points, x) for x in routes]
    footprints = [x for x in zip_longest(*footprints)]
    
    for robot_points in footprints:
        for key, value in Counter(robot_points).items():
            if key is not None and value > 1:
                answer += 1
        
    return answer
