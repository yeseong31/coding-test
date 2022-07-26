def solution(m, n, board):
    # 리스트 90도 회전
    def rotate(a):
        row, col = len(a), len(a[0])
        result = [[0] * row for _ in range(col)]
        for r in range(row):
            for c in range(col):
                result[c][row - 1 - r] = a[r][c]
        return result

    # 2x2 파악
    def check(x, y, b, v):
        if b[x][y] != '0' and b[x][y] == b[x + 1][y] == b[x][y + 1] == b[x + 1][y + 1]:
            v[x][y] = v[x + 1][y] = v[x][y + 1] = v[x + 1][y + 1] = 1
            return True
        return False

    # 삭제
    def delete(b, v):
        c = 0
        for i in range(n):
            for j in range(m - 1, -1, -1):
                if v[i][j] == 1:
                    v[i][j] = 0
                    b[i].pop(j)
                    b[i].append('0')
                    c += 1
        return c

    new_board = rotate([list(b) for b in board])
    visited = [[0] * m for _ in range(n)]

    cnt = 0
    answer = 0
    while True:
        for a in range(n - 1):
            for b in range(m - 1):
                if check(a, b, new_board, visited):
                    cnt += 1
        if cnt <= 0:
            break
        answer += delete(new_board, visited)
        cnt = 0

    return answer


board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
m, n = 4, 5
print(solution(m, n, board))
