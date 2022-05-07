def solution(key, lock):
    # key, lock의 길이
    m, n = len(key), len(lock)
    # key가 움직일 수 있는 범위만큼 자물쇠 영역을 넓혀야 함
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    # key를 돌려가면서, 움직이면서 체크
    for a in range(n * 2):
        for b in range(n * 2):
            for _ in range(4):
                key = rotation_key(key)
                # 키 삽입
                for i in range(m):
                    for j in range(m):
                        new_lock[i + a][j + b] += key[i][j]
                # 키 확인
                if check_lock(new_lock):
                    return True
                # 키 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[i + a][j + b] -= key[i][j]
    return False


# 자물쇠를 돌리는 함수(2차원 배열 회전)
def rotation_key(key):
    n = len(key)
    ret = [[0] * n for _ in range(n)]

    for r in range(n):
        for c in range(n):
            ret[c][n - 1 - r] = key[r][c]

    return ret


# 자물쇠에 열쇠가 들어맞는지 확인하는 함수
def check_lock(lock):
    n = len(lock) // 3
    for i in range(n, n * 2):
        for j in range(n, n * 2):
            if lock[i][j] != 1:
                return False
    return True