# 테트로미노
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]


# 시간: 6500ms
def rotate_a_matrix(a):
    result = [[0] * len(a) for _ in range(len(a[0]))]
    for r in range(len(a)):
        for c in range(len(a[0])):
            result[c][len(a) - 1 - r] = a[r][c]
    return result


def check(x, y, target):
    res = 0
    for i in range(len(target)):
        for j in range(len(target[0])):
            if target[i][j] == 1:
                res += board[x + i][y + j]
    return res


def checkL():
    res = 0
    blockA = [[1, 0], [1, 0], [1, 1]]
    blockB = [[0, 1], [0, 1], [1, 1]]
    for i in range(4):
        for x in range(n - len(blockA) + 1):
            for y in range(m - len(blockA[0]) + 1):
                res = max(res, check(x, y, blockA))
                res = max(res, check(x, y, blockB))
        if i < 3:
            blockA = rotate_a_matrix(blockA)
            blockB = rotate_a_matrix(blockB)
    return res


def checkZ():
    res = 0
    blockA = [[1, 0], [1, 1], [0, 1]]
    blockB = [[0, 1], [1, 1], [1, 0]]
    rotate = False
    for _ in range(2):
        for x in range(n - len(blockA) + 1):
            for y in range(m - len(blockA[0]) + 1):
                res = max(res, check(x, y, blockA))
                res = max(res, check(x, y, blockB))
        if not rotate:
            blockA = rotate_a_matrix(blockA)
            blockB = rotate_a_matrix(blockB)
            rotate = True
    return res


def checkI():
    res = 0
    block = [[1, 1, 1, 1]]
    rotate = False
    for _ in range(2):
        for x in range(n - len(block) + 1):
            for y in range(m - len(block[0]) + 1):
                res = max(res, check(x, y, block))
        if not rotate:
            block = rotate_a_matrix(block)
            rotate = True
    return res


def checkO():
    res = 0
    block = [[1, 1], [1, 1]]
    for x in range(n - len(block) + 1):
        for y in range(m - len(block[0]) + 1):
            res = max(res, check(x, y, block))
    return res


def checkT():
    res = 0
    block = [[1, 1, 1], [0, 1, 0]]
    for i in range(4):
        for x in range(n - len(block) + 1):
            for y in range(m - len(block[0]) + 1):
                res = max(res, check(x, y, block))
        if i < 3:
            block = rotate_a_matrix(block)
    return res


print(max(checkL(), checkZ(), checkI(), checkO(), checkT()))
