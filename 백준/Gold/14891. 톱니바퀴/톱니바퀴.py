import sys
from collections import deque

input = sys.stdin.readline

TOP = 0
LEFT = 6
RIGHT = 2


def check_left(target, direction):
    if target < 0 or cogwheels[target][RIGHT] == cogwheels[target + 1][LEFT]:
        return
    check_left(target - 1, -direction)
    cogwheels[target].rotate(direction)


def check_right(target, direction):
    if target >= 4 or cogwheels[target - 1][RIGHT] == cogwheels[target][LEFT]:
        return
    check_right(target + 1, -direction)
    cogwheels[target].rotate(direction)


cogwheels = [deque(list(input().strip())) for _ in range(4)]
result = [0] * 4
for _ in range(int(input().strip())):
    n, d = map(int, input().split())
    check_right(n, -d)
    check_left(n - 2, -d)
    cogwheels[n - 1].rotate(d)

answer = 0
base = 1
for i in range(4):
    answer += int(cogwheels[i][TOP]) * base
    base *= 2
print(answer)