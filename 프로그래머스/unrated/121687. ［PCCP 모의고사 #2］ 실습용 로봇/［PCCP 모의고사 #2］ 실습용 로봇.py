def solution(command):
    dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)
    x = y = d = 0
    
    for i in range(len(command)):
        cmd = command[i]
        if cmd == 'R':
            d = (d + 1) % 4
        elif cmd == 'L':
            d = (d - 1) % 4
        elif cmd == 'G':
            x, y = x + dx[d], y + dy[d]
        elif cmd == 'B':
            x, y = x - dx[d], y - dy[d]

    return x, y
