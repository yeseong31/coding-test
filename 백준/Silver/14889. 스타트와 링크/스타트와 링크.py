from itertools import combinations

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
sums = [sum(r) + sum(c) for r, c in zip(board, zip(*board))]

answer = 20001
for comb in list(combinations(range(n), n // 2)):
    red = blue = 0
    for i in range(n):
        if i in comb:
            red += sums[i]
        else:
            blue += sums[i]
    answer = min(answer, (abs(red - blue)) // 2)

print(answer)