from copy import deepcopy
from collections import deque


dx, dy = (0, 0, 1, 0, -1), (0, 1, 0, -1, 0)


def flip_board(case, x, y):
    result = deepcopy(case)
    for k in range(5):
        nx, ny = x + dx[k], y + dy[k]
        if nx < 0 or nx >= 3 or ny < 0 or ny >= 3:
            continue
        result[nx][ny] = '*' if case[nx][ny] == '.' else '.'
    return result


def to_binary(board):
    result = ''
    for i in range(3):
        for j in range(3):
            result += '0' if board[i][j] == '.' else '1'
    return int(result, 2)


def solution(case):
    board = [['.'] * 3 for _ in range(3)]
    q = deque([(0, board)])
    visited = [False] * 512
    visited[to_binary(board)] = True
    
    while q:
        count, board = q.popleft()
        if board == case:
            return count
        count += 1
        
        for x in range(3):
            for y in range(3):
                next_board = flip_board(board, x, y)
                board_binary = to_binary(next_board)
                
                if visited[board_binary]:
                    continue
                    
                q.append((count, next_board))
                visited[board_binary] = True
    
    return -1
    

for _ in range(int(input())):
    print(solution([list(input()) for _ in range(3)]))
