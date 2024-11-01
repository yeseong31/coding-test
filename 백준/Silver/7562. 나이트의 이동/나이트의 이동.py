from collections import deque

dist = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
for _ in range(int(input())):
    l = int(input())
    board = [[False] * l for _ in range(l)]
    x, y = map(int, input().split())
    tx, ty = map(int, input().split())

    q = deque()
    q.append((x, y, 0))
    board[x][y] = True
    while q:
        x, y, d = q.popleft()
        if x == tx and y == ty:
            print(d)
            break
        for dx, dy in dist:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= l or ny < 0 or ny >= l or board[nx][ny]:
                continue
            board[nx][ny] = True
            q.append((nx, ny, d + 1))