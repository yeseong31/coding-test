# 스타트링크
from collections import deque

# 총 f층, 출발, 목적, 위 u칸, 아래 d칸
f, s, g, u, d = map(int, input().split())

q = deque([(s, 0)])
visited = [False] * (f + 1)

answer = -1
while q:
    floor, cnt = q.popleft()
    if floor == g:
        answer = cnt
        break
    if floor <= 0 or floor > f or visited[floor]:
        continue
    visited[floor] = True
    q.append((floor + u, cnt + 1))
    q.append((floor - d, cnt + 1))

if answer == -1:
    print('use the stairs')
else:
    print(answer)
