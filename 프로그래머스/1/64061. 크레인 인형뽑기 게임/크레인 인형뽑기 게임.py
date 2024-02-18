def solution(board, moves):
    stack = []
    n = len(board)
    height = [0] * n
    cnt = 0

    for r in range(n):
        for c in range(n):
            if board[r][c] > 0:
                height[c] += 1

    for m in moves:
        if height[m - 1] == 0:
            continue
        
        catch = board[n - height[m - 1]][m - 1]
        board[n - height[m - 1]][m - 1] = 0
        height[m - 1] -= 1
        
        if stack and stack[-1] == catch:
            stack.pop()
            cnt += 2
        else:
            stack.append(catch)
        
    return cnt
