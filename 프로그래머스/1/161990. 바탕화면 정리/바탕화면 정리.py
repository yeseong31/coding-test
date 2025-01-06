def solution(wallpaper):
    lux = luy = 51
    rdx = rdy = -1
    
    n, m = len(wallpaper), len(wallpaper[0])
    
    for i in range(n):
        for j in range(m):
            if wallpaper[i][j] != '.':
                lux = min(lux, i)
                luy = min(luy, j)
                rdx = i + 1
                rdy = max(rdy, j + 1)
            
    return lux, luy, rdx, rdy
