from collections import deque


def check(a1, b1, a2, b2):
    res = 0
    prev = -1
    for i in range(a1, a2):
        for j in range(b1, b2):
            res += board[i][j]
            if prev == -1:
                prev = board[i][j]
                continue
            if prev != board[i][j]:
                return -1
    return res // ((a2 - a1) ** 2)


answer = [0, 0]
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
q = deque([(0, 0, n, n)])

while q:
    x1, y1, x2, y2 = q.popleft()
    if x2 - x1 == 1:
        answer[board[x1][y1]] += 1
        continue
    c = check(x1, y1, x2, y2)
    if c != -1:
        answer[c] += 1
        continue
    m = (x2 - x1) // 2
    q.append((x1, y1, x1 + m, y1 + m))
    q.append((x1, y1 + m, x1 + m, y2))
    q.append((x1 + m, y1, x2, y1 + m))
    q.append((x1 + m, y1 + m, x2, y2))

for x in answer:
    print(x)
