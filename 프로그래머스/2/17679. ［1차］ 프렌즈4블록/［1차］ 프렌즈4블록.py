def solution(m, n, board):
    def rotate(a):
        row, col = len(a), len(a[0])
        result = [[0] * row for _ in range(col)]
        for r in range(row):
            for c in range(col):
                result[c][row - 1 - r] = a[r][c]
        return result

    def check(x, y, b, v):
        if b[x][y] != '0' and b[x][y] == b[x + 1][y] == b[x][y + 1] == b[x + 1][y + 1]:
            v[x][y] = v[x + 1][y] = v[x][y + 1] = v[x + 1][y + 1] = 1
            return True
        else:
            return False

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

    cnt = answer = 0
    
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
