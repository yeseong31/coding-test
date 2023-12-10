def solution(board, aloc, bloc):
    n, m = len(board), len(board[0])
    dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)
    outside = lambda x, y: x < 0 or x >= n or y < 0 or y >= m
    
    def dfs(a, b, visited, step):
        x, y = a if step % 2 == 0 else b
        survive, must_lose = False, True
        win_left, lose_left = [], []
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if outside(nx, ny) or (nx, ny) in visited or board[nx][ny] == 0:
                continue
                
            survive = True
            if a == b:
                return True, step + 1
            
            next_step = [[nx, ny], b] if step % 2 == 0 else [a, [nx, ny]]
            win, left = dfs(*next_step, visited | {(x, y)}, step + 1)
            
            if win:
                win_left.append(left)
            else:
                lose_left.append(left)
            
            must_lose &= win
        
        if not survive:
            return False, step
        if must_lose:
            return False, max(win_left)
        
        return True, min(lose_left)
        
    return dfs(aloc, bloc, set(), 0)[1]
