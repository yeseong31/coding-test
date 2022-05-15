# 예제 4-1 상하좌우(110p)

n = int(input())
data = input().split()
x, y = 1, 1

decision = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for d in data:
    for i in range(len(decision)):
        if d == decision[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x, y = nx, ny

print(x, y)
