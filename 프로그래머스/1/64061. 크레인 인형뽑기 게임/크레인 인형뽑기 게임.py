def solution(board, moves):
    stack = []
    height = [0] * len(board)
    cnt = 0

    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] > 0:
                height[c] += 1

    for m in moves:
        if height[m - 1] == 0:
            continue
        
        catch = board[len(board) - height[m - 1]][m - 1]
        board[len(board) - height[m - 1]][m - 1] = 0
        height[m - 1] -= 1
        
        if stack and stack[-1] == catch:
            stack.pop()
            cnt += 2
        else:
            stack.append(catch)
        
    return cnt
