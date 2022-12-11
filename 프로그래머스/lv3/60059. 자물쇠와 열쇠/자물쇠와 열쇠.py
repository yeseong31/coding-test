def solution(key, lock):
    def rotate_key():
        result = [[0] * len(key) for _ in range(len(key[0]))]
        for r in range(len(key)):
            for c in range(len(key[0])):
                result[c][len(key) - 1 - r] = key[r][c]
        return result
    
    def check_key():
        for i in range(m - 1, m + n - 1):
            for j in range(m - 1, m + n - 1):
                if board[i][j] != 1:
                    return False
        return True
    
    n, m = len(lock), len(key)
    board = [[0] * (n + 2 * (m - 1)) for _ in range(n + 2 * (m - 1))]
    
    for i in range(m - 1, m + n - 1):
        for j in range(m - 1, m + n - 1):
            board[i][j] = lock[i - m + 1][j - m + 1]
            
    for i in range(n + m - 1):
        for j in range(n + m - 1):
            for _ in range(4):
                # 키 삽입
                for x in range(m):
                    for y in range(m):
                        board[i + x][j + y] += key[x][y]
                # 키 확인
                if check_key():
                    return True
                # 키 추출
                for x in range(m):
                    for y in range(m):
                        board[i + x][j + y] -= key[x][y]
                # 키 회전
                key = rotate_key()

    return False