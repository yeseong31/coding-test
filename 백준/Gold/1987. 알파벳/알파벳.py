def dfs(x, y, d):
    global answer
    answer = max(answer, d)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue
        target = board[nx][ny]
        if alpha[find_index(target)] != 0:
            continue
        alpha[find_index(target)] += 1
        dfs(nx, ny, d + 1)
        alpha[find_index(target)] -= 1


def find_index(c):
    return ord(c) - ord('A')


answer = 0

r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
alpha = [0] * 26
alpha[find_index(board[0][0])] += 1

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

dfs(0, 0, 1)

print(answer)