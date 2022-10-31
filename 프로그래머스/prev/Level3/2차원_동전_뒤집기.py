import copy


def solution(beginning, target):
    INF = int(1e9)

    def change(i, j, board):
        if board[i][j] == 0:
            board[i][j] = 1
        else:
            board[i][j] = 0

    def check(a, b):
        res = 0
        board = copy.deepcopy(beginning)

        if a:
            res += 1
            for j in range(m):
                change(0, j, board)
        if b:
            res += 1
            for i in range(n):
                change(i, 0, board)

        for i in range(1, n):
            if board[i][0] != target[i][0]:
                res += 1
                for j in range(m):
                    change(i, j, board)
        for j in range(1, m):
            if board[0][j] != target[0][j]:
                res += 1
                for i in range(n):
                    change(i, j, board)

        for i in range(n):
            for j in range(m):
                if board[i][j] != target[i][j]:
                    return INF
        return res

    answer = INF
    n, m = len(beginning), len(beginning[0])
    if beginning[0][0] != target[0][0]:
        answer = min(answer, check(0, 1), check(1, 0))
    else:
        answer = min(answer, check(0, 0), check(1, 1))

    if answer == INF:
        return -1
    return answer
