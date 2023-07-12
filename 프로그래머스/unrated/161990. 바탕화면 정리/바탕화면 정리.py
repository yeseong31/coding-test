def solution(wallpaper):
    lux = luy = 51
    rdx = rdy = -1
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '.':
                continue
            lux = min(lux, i)
            luy = min(luy, j)
            rdx = i + 1
            rdy = max(rdy, j + 1)
            
    return [lux, luy, rdx, rdy]