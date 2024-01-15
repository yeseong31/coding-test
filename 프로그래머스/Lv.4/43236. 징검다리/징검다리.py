def is_passable(target_distance, rocks, n):
    removed = last = 0
    
    for rock in rocks:
        if rock - last < target_distance:
            removed += 1
            continue
        last = rock
        
    return removed <= n


def solution(distance, rocks, n):
    rocks.append(distance)
    rocks.sort()
    
    min_distance, max_distance = 1, distance + 1
    
    while min_distance + 1 < max_distance:
        target_distance = (min_distance + max_distance) // 2
        
        if is_passable(target_distance, rocks, n):
            min_distance = target_distance
        else:
            max_distance = target_distance
    
    return min_distance
