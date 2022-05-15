"""
감시 피하기 (351p)
"""


import copy

# 복도의 크기
n = int(input())
# 복도 - 선생님: T / 학생: S / 빈 칸: X
area = []
teachers = []
for i in range(n):
    row = list(map(str, input().split()))
    for j, v in enumerate(row):
        if v == 'T':
            teachers.append((i, j))
    area.append(row)


def dfs(i, x, y, c):
    global check
    nx = x + dx[i]
    ny = y + dy[i]

    # 감시가 불가능한 영역이거나 장애물에 가로막히거나 선생님들끼리 감시 구역이 겹친다면
    if nx < 0 or nx >= n or ny < 0 or ny >= n or c[nx][ny] == 'O':
        # 해당 방향으로의 감시를 멈추고 방향을 바꾼 뒤 다시 확인해야 함
        return
    # 만약 학생이 발각되면 True
    if c[nx][ny] == 'S':
        check = True
        return
    # 그렇지 않으면 해당 위치를 '선생님'으로 바꾼 후 똑같은 과정 반복
    c[nx][ny] = 'T'
    dfs(i, nx, ny, c)
    return


# 감시 방향을 고정(d)한 상태에서 해당 위치부터 감시 시작
def keep_watch():
    check_area = copy.deepcopy(area)

    # 선생님 한 사람씩 상하좌우로 감시 수행
    for a, b in teachers:
        for d in range(4):
            dfs(d, a, b, check_area)

    return check


def createWall(cnt):
    global result, check
    # 벽 3개를 다 설치했으면
    if cnt == 3:
        # 선생님들이 학생들을 발견하지 못 했다면 성공
        if not keep_watch():
            result = True
        # check는 원래대로
        check = False
    else:
        for i in range(n):
            for j in range(n):
                if area[i][j] == 'X':
                    area[i][j] = 'O'
                    createWall(cnt + 1)
                    area[i][j] = 'X'


# 고정된 위치에서 복도 끝까지 상하좌우로 감시해야 함
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# check: 벽을 설치하는 경우의 수마다 확인
# result: 전체 경우의 수에 대해 한 번이라도 학생들이 발각되지 않는 경우 True, 아니면 False
check = False
result = False
createWall(0)

if result:
    print('YES')
else:
    print('NO')
