from collections import deque


def solution():
    n = int(input())
    x, y = map(int, input().split())
    convenience_stores = [tuple(map(int, input().split())) for _ in range(n)]
    fx, fy = map(int, input().split())
    
    q = deque([(x, y)])
    visited = [False] * n
    
    while q:
        x, y = q.popleft()
        if abs(x - fx) + abs(y - fy) <= 1000:
            return 'happy'
        
        for i in range(n):
            if visited[i]:
                continue
                
            nx, ny = convenience_stores[i]
            if abs(x - nx) + abs(y - ny) <= 1000:
                visited[i] = True
                q.append((nx, ny))
        
    return 'sad'


for _ in range(int(input())):
    print(solution())
