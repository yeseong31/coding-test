"""
블록 이동하기 (355p)

https://programmers.co.kr/learn/courses/30/lessons/60063
"""
import collections


def get_next_position(pos, board):
    next_position = []

    x1, y1 = pos[0]
    x2, y2 = pos[1]

    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx1, ny1, nx2, ny2 = x1 + dx[i], y1 + dy[i], x2 + dx[i], y2 + dy[i]
        # 이동할 수 있다면
        if board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
            next_position.append([(nx1, ny1), (nx2, ny2)])
    # 로봇이 '가로'로 놓여 있다면
    if x1 == x2:
        # 위쪽으로 회전 또는 아래쪽으로 회전
        for i in [-1, 1]:
            # 위쪽/아래쪽 두 칸이 모두 비어 있다면
            if board[x1 + i][y1] == 0 and board[x2 + i][y2] == 0:
                next_position.append([(x1, y1), (x1 + i, y1)])
                next_position.append([(x2, y2), (x2 + i, y2)])
    # 로봇이 '세로'로 놓여 있다면
    elif y1 == y2:
        # 왼쪽으로 회전 또는 오른쪽으로 회전
        for i in [-1, 1]:
            # 왼쪽/오른쪽 두 칸이 모두 비어 있다면
            if board[x1][y1 + i] == 0 and board[x2][y2 + i] == 0:
                next_position.append([(x1, y1), (x1, y1 + i)])
                next_position.append([(x2, y2), (x2, y2 + i)])

    return next_position


def solution(board):
    answer = 0
    n = len(board)

    # 상하좌우로 한 칸씩 늘린 새로운 board 생성
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]

    # 로봇이 이동 가능한 곳
    q = collections.deque()
    # 방문 처리
    visited = []
    # 처음 위치
    position = [(1, 1), (1, 2)]
    q.append((position, 0))    # (위치, 이동 횟수)
    visited.append(position)

    # bfs 수행
    while q:
        pos, cnt = q.popleft()
        # (n, n) 위치에 도달했다면 cnt 반환
        if (n, n) in pos:
            return cnt
        for n_pos in get_next_position(pos, new_board):
            if n_pos not in visited:
                q.append((n_pos, cnt + 1))
                visited.append(n_pos)

    return answer


board = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
print(solution(board))    # 7
