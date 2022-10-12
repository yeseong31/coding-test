from collections import deque

for _ in range(int(input())):
    n = int(input())
    blocks = deque(list(map(int, input().split())))
    first = max(blocks[0], blocks[-1])
    stack = []

    answer = 'Yes'
    while blocks:
        if blocks[0] < blocks[-1]:
            p = blocks.pop()
        else:
            p = blocks.popleft()
        if stack and stack[-1] < p:
            answer = 'No'
            break
        stack.append(p)

    print(answer)