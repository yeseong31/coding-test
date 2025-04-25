def solution(n):
    answer = [[0] * i for i in range(1, n + 1)]
    
    dx, dy = (1, 0, -1), (0, 1, -1)
    x, y = -1, 0
    count = 1
    
    for i in range(n):
        for j in range(i, n):
            x, y = x + dx[i % 3], y + dy[i % 3]
            answer[x][y] = count
            count += 1
    
    return [k for row in answer for k in row]
