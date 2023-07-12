def solution(park, routes):
    direction = {'E': (0, 1), 'S': (1, 0), 'W': (0, -1), 'N': (-1, 0)}
    
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                x, y = i, j
                break
    
    for route in routes:
        d, v = route.split()
        nx, ny = x, y
        check = False
        
        for i in range(int(v)):
            nx, ny = nx + direction[d][0], ny + direction[d][1]
            if nx < 0 or nx >= len(park) or ny < 0 or ny >= len(park[0]) or park[nx][ny] == 'X':
                check = True
                break

        if not check:
            x, y = nx, ny
    
    return [x, y]