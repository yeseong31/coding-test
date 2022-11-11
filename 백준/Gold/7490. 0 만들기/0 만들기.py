from collections import deque


def bfs(n):
    q = deque(['1'])
    answer = []
    while q:
        exp = q.popleft()
        prev = int(exp[-1])
        if prev == n:
            if eval(exp.replace(' ', '')) == 0:
                answer.append(exp)
            continue
        for op in ['+', '-', ' ']:
            q.append(f'{exp}{op}{prev + 1}')
    return sorted(answer)
    

for _ in range(int(input())):
    for target in bfs(int(input())):
        print(target)
    print()