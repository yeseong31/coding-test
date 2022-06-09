import collections


def solution(maps):
    def bfs(x, y):
        q = collections.deque()
        q.append((x, y))

        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                # 범위 밖이거나 벽으로 막혀 있는 경우
                if nx < 0 or nx >= n or ny < 0 or ny >= m or maps[nx][ny] == 0:
                    continue
                # 경유한 적이 없는 경우
                elif maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    q.append((nx, ny))

    # 방향
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    # 맵의 크기
    n, m = len(maps), len(maps[0])
    # 시작 위치
    maps[0][0] += 1
    # DFS 수행
    bfs(0, 0)

    target = maps[n - 1][m - 1]
    # 목적지에 도달하지 못한 경우
    if target == 1:
        return -1
    return target - 1


maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]
print(solution(maps))
