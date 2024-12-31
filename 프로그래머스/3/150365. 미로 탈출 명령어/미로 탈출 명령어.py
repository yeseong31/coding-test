from collections import deque


def solution(n, m, x, y, r, c, k):
    dx = (1, 0, 0, -1)
    dy = (0, -1, 1, 0)
    dz = ('d', 'l', 'r', 'u')
    q = deque([(x, y, '')])
    
    while q:
        x, y, result = q.popleft()
        
        if (x, y) == (r, c):
            if k % 2 != len(result) % 2:
                break
            if len(result) == k:
                return result
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 < nx <= n and 0 < ny <= m and len(result) + abs(nx - r) + abs(ny - c) < k:
                q.append((nx, ny, result + dz[i]))
                break
                
    return 'impossible'
