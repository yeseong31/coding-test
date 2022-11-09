import sys
from collections import deque

input = sys.stdin.readline


def rotate_matrix(a):
    row, col = len(a), len(a[0])
    result = [deque([0] * 12) for _ in range(6)]
    for r in range(12):
        for c in range(6):
            result[c][row - 1 - r] = a[r][c]
    return result


def bfs(x, y, p):
    color = board[x][y]
    q.append((x, y))
    p.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= 6 or ny < 0 or ny >= 12:
                continue
            if board[nx][ny] != color or (nx, ny) in p or visited[nx][ny]:
                continue
            visited[nx][ny] = True
            p.append((nx, ny))
            q.append((nx, ny))
    return p
    

board = rotate_matrix([list(input()) for _ in range(12)])
dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

answer = 0
q = deque()
points = []

while True:
    visited = [[False] * 12 for _ in range(6)]
    check = False
    for i in range(6):
        for j in range(12):
            if board[i][j] == '.':
                break
            if visited[i][j]:
                continue
            p = bfs(i, j, [])
            if len(p) >= 4:
                points.extend(p)
                check = True
    if not check:
        break
    answer += 1
    while points:
        x, y = points.pop()
        board[x][y] = '.'
    for i in range(6):
        stack = []
        for _ in range(12):
            b = board[i].popleft()
            if b == '.':
                board[i].append(b)
            else:
                stack.append(b)
        while stack:
            board[i].appendleft(stack.pop())
            
print(answer)
