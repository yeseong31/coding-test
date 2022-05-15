"""
인구 이동 (353p)
"""
import collections

# 땅의 크기, L명 이상, R명 이하
n, l, r = map(int, input().split())
# 각 나라의 인구 수
country = []
for _ in range(n):
    country.append(list(map(int, input().split())))

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(a, b, c):
    # bfs 큐
    q = collections.deque()
    q.append((a, b))
    # 연합된 나라들
    union = [(a, b)]
    # 방문한 나라에 대해 번호 표시
    visited[a][b] = c
    # 해당 연합의 인구 수
    sum_population = country[a][b]

    while q:
        x, y = q.popleft()
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]

            # 영역 밖의 공간이라면 탐색하지 않음
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            # 방문하지 않은 장소에 한해 l이상 r 이하인 경우에 대해서만 개방(리스트에 좌표 삽입)
            if visited[nx][ny] == -1 and l <= abs(country[x][y] - country[nx][ny]) <= r:
                # 방문 처리, 큐 및 리스트에 해당 국가 추가
                visited[nx][ny] = c
                q.append((nx, ny))
                union.append((nx, ny))
                sum_population += country[nx][ny]

    # union에 속한 나라들에 대해 인구 이동 수행
    for i, j in union:
        country[i][j] = sum_population // len(union)

    # 연합된 나라들의 수를 반환
    return len(union)


days = 0
# 더 이상 인구 이동이 없을 때까지 반복
while True:
    # 방문 표시
    visited = [[-1] * n for _ in range(n)]
    # 연합된 나라들을 구분
    cnt = 0

    # 모든 칸에 대해
    q = collections.deque()
    for x in range(n):
        for y in range(n):
            # 아직 방문하지 않은 곳이라면
            if visited[x][y] == -1:
                bfs(x, y, cnt)
                cnt += 1

    # 만약 모든 칸에 대해 연합된 나라가 없다면 (모든 나라가 독립된 나라라면)
    if cnt == n * n:
        break
    days += 1

print(days)
