def solution(dirs):
    x, y = 0, 0
    visited = set()

    for c in dirs:
        if c == 'U' and y < 5:
            visited.add(((x, y), (x, y + 1)))
            y += 1
        if c == 'D' and y > -5:
            visited.add(((x, y - 1), (x, y)))
            y -= 1
        if c == 'R' and x < 5:
            visited.add(((x, y), (x + 1, y)))
            x += 1
        if c == 'L' and x > -5:
            visited.add(((x - 1, y), (x, y)))
            x -= 1
    
    return len(visited)
