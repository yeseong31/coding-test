"""
감시 피하기 - 풀이
"""


# 복도의 크기
import itertools

n = int(input())
# 복도의 정보
board = []
teachers = []
spaces = []
for i in range(n):
    board.append(list(map(str, input().split())))
    for j in range(n):
        if board[i][j] == 'T':
            teachers.append((i, j))
        if board[i][j] == 'X':
            spaces.append((i, j))


def find_student(x, y):
    if board[x][y] == 'S':
        return True
    if board[x][y] == 'O':
        return False


# 특정 방향으로 감시 진행 (학생 발견 시 True)
def watch(x, y, direction):
    if direction == 0:
        while y >= 0:
            find_student(x, y)
            y -= 1
    elif direction == 1:
        while y < n:
            find_student(x, y)
            y += 1
    elif direction == 2:
        while x >= 0:
            find_student(x, y)
            x -= 1
    elif direction == 3:
        while x < n:
            find_student(x, y)
            x += 1
    return False


# 장애물 설치 이후, 한 명이라도 학생이 감지되는지 검사
def process():
    for x, y in teachers:
        for i in range(4):
            if watch(x, y, i):
                return True
    return False


find = False

# 파이썬 조합 이용
for data in itertools.combinations(spaces, 3):
    for x, y in data:
        board[x][y] = 'O'
    if not process():
        find = True
        break
    for x, y in data:
        board[x][y] = 'X'

if find:
    print('YES')
else:
    print('NO')
