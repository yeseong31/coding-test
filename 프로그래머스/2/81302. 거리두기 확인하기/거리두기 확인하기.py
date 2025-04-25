def solution(places):
    dx = (-1, 0, 1, 0, -1, 1, 1, -1, -2, 0, 2, 0)  
    dy = (0, 1, 0, -1, 1, 1, -1, -1, 0, 2, 0, -2)
    
    return [check_place(p, dx, dy) for p in places]


def check_place(place, dx, dy):
    p_points = [(x, y) for x in range(5) for y in range(5) if place[x][y] == 'P']
    
    for x, y in p_points:
        for i in range(12):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5 or place[nx][ny] != 'P':
                continue

            dist_x, dist_y = abs(nx - x), abs(ny - y)

            # x축으로 두 칸 이동
            if dist_x == 2:
                if place[x - 1 if nx < x else x + 1][ny] == 'O':
                    return 0
            # y축으로 두 칸 이동
            elif dist_y == 2:
                if place[nx][y - 1 if ny < y else y + 1] == 'O':
                    return 0
            # 대각선으로 한 칸 이동
            elif dist_x == dist_y == 1:
                if not place[nx][y] == place[x][ny] == 'X':
                    return 0
            # 한 칸 이동 시
            elif place[nx][ny] == 'P':
                return 0
            
    return 1
