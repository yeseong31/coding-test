# 직각이등변삼각형찾기
# https://www.acmicpc.net/problem/2658

def solution():
    def dfs(x, y, v):
        if x < 0 or x >= 10 or y < 0 or y >= 10 or visited[x][y] or board[x][y] != v:
            return
        visited[x][y] = True
        dfs(x, y - 1, v)
        dfs(x, y + 1, v)
        dfs(x - 1, y, v)
        dfs(x + 1, y, v)

    def check(arr):
        if len(arr) < 2 or len(arr) > 10:
            return False

        length = [len(x) for x in arr]
        if length[0] == length[-1]:
            left, right = 0, len(length) - 1
            c = 0
            while left < right:
                l, r = length[left], length[right]
                if not (l == r == c + 1):
                    return False
                left += 1
                right -= 1
                c += 1
            if left == right and length[left] == length[right] == c + 1:
                return True
            return False

        length.sort()
        if length == list(range(1, length[-1] + 1, 1)) or length == list(range(1, length[-1] + 1, 2)):
            return True
        return False

    board = [[0] * 10 for _ in range(10)]
    one = []
    for i in range(10):
        tmp = []
        for j, k in enumerate(input()):
            if k == '1':
                tmp.append((i, j))
                board[i][j] = int(k)
        if tmp:
            one.append(tmp)
    visited = [[False] * 10 for _ in range(10)]

    count = 0
    for i in range(10):
        for j in range(10):
            if not visited[i][j]:
                dfs(i, j, board[i][j])
                if board[i][j] == 1:
                    count += 1

    if not count == 1 or not check(one):
        print(0)
        return

    point = sorted(one, key=lambda x: len(x), reverse=True)
    answer = [point.pop()[0]]

    if len(point[-1]) == 1:
        answer.append(point.pop()[0])
        tmp = point[0]
        if answer[0][1] == tmp[0][1]:
            answer.append(tmp[-1])
        else:
            answer.append(tmp[0])
    else:
        answer.append(point[0][0])
        answer.append(point[0][-1])

    for a, b in sorted(answer):
        print(a + 1, b + 1)
    return


solution()
