def solution(dirs):
    # 시작 위치
    x, y = 0, 0
    # 방문 처리
    visited = set()

    for c in dirs:
        if c == 'U' and y < 5:
            visited.add(((x, y), (x, y + 1)))
            y += 1
        elif c == 'D' and y > -5:
            visited.add(((x, y - 1), (x, y)))
            y -= 1
        elif c == 'R' and x < 5:
            visited.add(((x, y), (x + 1, y)))
            x += 1
        elif c == 'L' and x > -5:
            visited.add(((x - 1, y), (x, y)))
            x -= 1
    return len(visited)


dirs = "LULLLLLLU"
print(solution(dirs))
