# 실전 문제 3 - 게임 개발(118p)

# 맵의 세로 크기, 맵의 가로 크기
n, m = map(int, input().split())
# 캐릭터의 좌표(a, b), 방향 d
a, b, d = map(int, input().split())

# 게임 맵
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
# 방문 흔적
visited = [[0] * m for _ in range(n)]
# 현재 위치 방문 처리
visited[a][b] = 1

# 방향(북, 동, 남, 서)
da = [-1, 0, 1, 0]
db = [0, 1, 0, -1]


def decide_the_direction():
    global d
    d -= 1
    if d < 0:
        d = 3


count = 1
turn_count = 0
while True:
    # 방향: 현재 방향을 기준으로 왼쪽 방향부터 차례대로 갈 곳을 정함 ----- 1단계
    # 왼쪽으로 한 번 회전했을 때 ----- 2단계
    decide_the_direction()
    na = a + da[d]
    nb = b + db[d]
    # 그 방향에 아직 가보지 않은 칸이 존재한다면 한 칸 전진
    if data[na][nb] == 0 and visited[na][nb] == 0:
        a, b = na, nb
        data[a][b] = 1
        turn_count = 0
        count += 1
        continue
    # 그렇지 않다면 회전 횟수 1 증가
    else:
        turn_count += 1
    # 만약 네 방향 모두 이미 가본 칸이거나 바다(1)로 되어 있으면,
    # 방향을 유지한 채 한 칸 뒤로 이동 후 1단계로 돌아감
    if turn_count == 4:
        na = a - da[d]
        nb = b - db[d]
        if data[na][nb] == 0:
            a, b = na, nb
        else:
            break
        turn_count = 0

print(count)
