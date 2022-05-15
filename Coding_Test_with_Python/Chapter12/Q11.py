"""
뱀 (327p)
"""

# 보드의 크기
n = int(input())
# 사과의 개수
k = int(input())

# 게임 맵
gameMap = [[0] * (n + 1) for _ in range(n + 1)]
# 사과의 위치
for _ in range(k):
    a, b = map(int, input().split())
    gameMap[a][b] = 1

# 뱀의 방향 변환 횟수
l = int(input())
# 뱀의 방향 변환 정보
data = []
for _ in range(l):
    x, c = input().split()
    data.append((int(x), c))

# 방향(북, 동, 남, 서)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


# 방향 회전
def rotate(d: int, ch) -> int:
    if ch == 'L':
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4
    return d


# 게임 실행
def simulation():
    # 초기 위치
    x, y = 1, 1
    # 초기 위치 방문 표시
    gameMap[x][y] = 2
    # 초기 방향(동쪽)
    d = 0
    # 게임 진행 시간
    time = 0
    # 뱀의 회전 횟수
    cnt = 0
    # 뱀 정보
    q = [(x, y)]

    while True:
        nx, ny = x + dx[d], y + dy[d]
        time += 1
        # 범위를 벗어나거나 자신과 부딪힌다면 게임이 끝남
        if nx < 1 or n < nx or ny < 1 or n < ny or gameMap[nx][ny] == 2:
            break
        # 만약 이동한 칸에 사과가 없다면
        if gameMap[nx][ny] != 1:
            # 몸길이를 줄여서 꼬리가 위치한 칸을 비워줌
            gameMap[nx][ny] = 2
            a, b = q.pop(0)
            gameMap[a][b] = 0
        # 머리를 다음 칸에 위치
        q.append((nx, ny))
        x, y = nx, ny
        # 게임 시작시간으로부터 x초가 끝난 뒤 회전
        if cnt < l and time == data[cnt][0]:
            d = rotate(d, data[cnt][1])
            cnt += 1
    return time


print(simulation())