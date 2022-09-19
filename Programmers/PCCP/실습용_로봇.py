def solution(command):
    x = y = 0
    d = 0
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for c in command:
        if c == 'L':
            d -= 1
        elif c == 'R':
            d += 1
        else:
            dx, dy = direction[d % 4]
            if c == 'B':
                dx, dy = -dx, -dy
            x, y = x + dx, y + dy

    return x, y
