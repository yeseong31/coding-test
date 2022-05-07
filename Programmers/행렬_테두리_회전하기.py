def solution(rows, columns, queries):
    board = [[0] * (columns + 1) for _ in range(rows + 1)]
    t = 1
    for row in range(1, rows + 1):
        for col in range(1, columns + 1):
            board[row][col] = t
            t += 1

    answer = []
    for x1, y1, x2, y2 in queries:
        backup_value = board[x1][y1]
        min_value = backup_value

        # 왼쪽 세로 줄
        for z in range(x1, x2):
            board[z][y1] = board[z + 1][y1]
            min_value = min(min_value, board[z + 1][y1])
        # 아래쪽 가로 줄
        for z in range(y1, y2):
            board[x2][z] = board[x2][z + 1]
            min_value = min(min_value, board[x2][z + 1])
        # 오른쪽 세로 줄
        for z in range(x2, x1, -1):
            board[z][y2] = board[z - 1][y2]
            min_value = min(min_value, board[z - 1][y2])
        # 위쪽 가로 줄
        for z in range(y2, y1, -1):
            board[x1][z] = board[x1][z - 1]
            min_value = min(min_value, board[x1][z - 1])
        board[x1][y1 + 1] = backup_value

        answer.append(min_value)

    return answer