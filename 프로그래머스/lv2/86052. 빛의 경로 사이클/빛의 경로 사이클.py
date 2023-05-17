def solution(grid):
    def dfs(sx, sy, sd):
        x, y, d = sx, sy, sd
        cnt = 0
        visited[sx][sy][sd] = 1

        while True:
            nx = (x + dx[d]) % len(grid)
            ny = (y + dy[d]) % len(grid[0])
            cnt += 1

            if grid[nx][ny] == 'R':
                d = (d + 1) % 4
            elif grid[nx][ny] == 'L':
                d = (d - 1) % 4
            if visited[nx][ny][d]:
                if (nx, ny, d) == (sx, sy, sd):
                    return cnt
                return 0

            visited[nx][ny][d] = 1
            x, y = nx, ny

    dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
    visited = [[[0] * 4 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    answer = []

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for k in range(4):
                if not visited[i][j][k]:
                    if dist := dfs(i, j, k):
                        answer.append(dist)

    return sorted(answer)