def solution(m, n, startX, startY, balls):
    def check_dist(x, y):
        dx, dy = (2 * (m - x), -2 * x, 0, 0), (0, 0, 2 * (n - y), -2 * y)
        dist = int(1e6)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            ns = abs(x - nx) ** 2 + abs(y - ny) ** 2
            ne = abs(startX - nx) ** 2 + abs(startY - ny) ** 2
            if (startX == nx == x or startY == ny == y) and ns <= ne:
                continue
            dist = min(dist, ne)
        return dist
            
    return [check_dist(a, b) for a, b in balls]


