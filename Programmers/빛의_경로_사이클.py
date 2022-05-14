def solution(grid):
    def dfs(sx, sy, sd):
        # 사용할 좌표
        x, y, d = sx, sy, sd
        # 거리 계산
        cnt = 0
        # 방문 표시
        visited[sx][sy][sd] = 1

        while True:
            nd = d
            nx = (x + dx[nd]) % len(grid)
            ny = (y + dy[nd]) % len(grid[0])
            cnt += 1

            # 오른쪽
            if grid[nx][ny] == 'R':
                nd = (d + 1) % 4
            # 왼쪽
            elif grid[nx][ny] == 'L':
                nd = (d - 1) % 4
            # 해당 위치를 이미 방문했었다면
            if visited[nx][ny][nd]:
                # 시작 위치와 같다면 사이클 발생
                if (nx, ny, nd) == (sx, sy, sd):
                    return cnt
                # 그렇지 않으면 사이클이 아니므로 0 반환
                else:
                    return 0

            visited[nx][ny][nd] = 1
            x, y, d = nx, ny, nd

    # 방향 (북, 동, 남, 서)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 방문 (3차원 배열)
    visited = [[[0] * 4 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    answer = []

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for k in range(4):
                # 만약 방문하지 않았다면
                if not visited[i][j][k]:
                    if dist := dfs(i, j, k):
                        answer.append(dist)

    return sorted(answer)


grid =	["SL", "LR"]
print(solution(grid))
