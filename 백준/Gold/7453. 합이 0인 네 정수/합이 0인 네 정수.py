import sys
from itertools import product

input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

target = range(n)
ab, cd = [], []
for x, y in product(target, target):
    ab.append(board[x][0] + board[y][1])
    cd.append(board[x][2] + board[y][3])

ab.sort()
cd.sort(reverse=True)

answer = p = q = 0
while p < len(ab) and q < len(cd):
    if ab[p] + cd[q] == 0:
        x = 1
        for i in range(p + 1, len(ab)):
            if ab[p] != ab[i]:
                break
            x += 1
        y = 1
        for j in range(q + 1, len(cd)):
            if cd[q] != cd[j]:
                break
            y += 1
        answer += x * y
        p += x
        q += y
    elif ab[p] + cd[q] < 0:
        p += 1
    else:
        q += 1

print(answer)
