def check(board, x=None, y=None) -> int:
    result = count = 0
    prev = ''
    
    for i in range(len(board)):
        target = board[x][i] if y is None else board[i][y]
        if prev == '' or prev == target:
            count += 1
        else:
            result = max(result, count)
            count = 1
        prev = target
        
    return max(result, count)


def solution() -> int:
    answer = 0
    n = int(input())
    board = [list(input()) for _ in range(n)]
    
    for x in range(n):
        for y in range(n):
            if y + 1 < n:
                board[x][y], board[x][y + 1] = board[x][y + 1], board[x][y]
                answer = max(answer, check(board, x=x), check(board, y=y), check(board, y=y + 1))
                board[x][y], board[x][y + 1] = board[x][y + 1], board[x][y]
            if x + 1 < n:
                board[x][y], board[x + 1][y] = board[x + 1][y], board[x][y]
                answer = max(answer, check(board, y=y), check(board, x=x), check(board, x=x + 1))
                board[x][y], board[x + 1][y] = board[x + 1][y], board[x][y]
            
    return answer


print(solution())