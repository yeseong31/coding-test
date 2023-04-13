from collections import deque


def solution(n, m, x, y, r, c, k):
    answer = 'z' * k
    dx, dy, dz = (1, 0, 0, -1), (0, -1, 1, 0), ('d', 'l', 'r', 'u')
    q = deque([(x, y, '')])
    
    while q:
        x, y, result = q.popleft()
        if x == r and y == c:
            if (k - len(result)) % 2 == 1:
                return 'impossible'
            if len(result) == k:
                return result
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx <= 0 or nx > n or ny <= 0 or ny > m:
                continue
            if abs(nx - r) + abs(ny - c) + len(result) + 1 > k:
                continue
            q.append((nx, ny, result + dz[i]))
            break
                
    return 'impossible'
