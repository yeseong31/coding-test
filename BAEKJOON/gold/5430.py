# AC
import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    p = input()
    n = int(input())
    s = input().rstrip()
    if len(s) > 2:
        s = list(map(int, s[1:-1].split(',')))
        x = deque(s)
    else:
        x = []

    cnt = 0
    flag = True
    for target in p:
        if target == 'R':
            cnt += 1
        elif target == 'D':
            if len(x) == 0:
                flag = False
                break
            if cnt % 2 == 0:
                x.popleft()
            else:
                x.pop()

    if not flag:
        print('error')
        continue
    if len(x) == 0:
        print('[]')
        continue
    answer = ''
    if cnt % 2 == 1:
        for i in range(len(x) - 1, -1, -1):
            answer += f'{str(x[i])},'
    else:
        for i in range(len(x)):
            answer += f'{str(x[i])},'
    print(f'[{answer[:-1]}]')
