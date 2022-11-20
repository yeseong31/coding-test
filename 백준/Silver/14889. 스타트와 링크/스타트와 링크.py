import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
sums = [sum(r) + sum(c) for r, c in zip(board, zip(*board))]
total = sum(sums)

answer = 20001
for comb in list(combinations(range(n), n // 2)):
    red = sum([sums[i] for i in range(n) if i in comb])
    answer = min(answer, (abs(total - 2 * red)) // 2)

print(answer)