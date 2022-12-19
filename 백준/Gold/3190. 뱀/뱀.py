from collections import deque

n = int(input())
board = [[0] * n for _ in range(n)]

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)
d = 0

for _ in range(int(input())):
    a, b = map(int, input().split())
    board[a - 1][b - 1] = 2
    
r = int(input())
commands = [(input().split()) for _ in range(r)]

x = y = 0
q = deque([(x, y)])
board[0][0] = 1

t = cnt = 0
while True:
    nx, ny = x + dx[d], y + dy[d]
    t += 1
    
    if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] == 1:
        break
    if board[nx][ny] != 2:
        a, b = q.popleft()
        board[a][b] = 0
        
    board[nx][ny] = 1
    q.append((nx, ny))
    x, y = nx, ny
    
    if cnt < r and t == int(commands[cnt][0]):
        if commands[cnt][1] == 'D':
            d = (d + 1) % 4
        else:
            d = (d - 1) % 4
        cnt += 1
        
print(t)
