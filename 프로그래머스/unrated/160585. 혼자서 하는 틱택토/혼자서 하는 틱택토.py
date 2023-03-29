def check(board, tboard, x):
    for i in range(3):
        if board[i] == x or tboard[i] == x:
            return True
    return f'{board[0][0]}{board[1][1]}{board[2][2]}' == x \
            or f'{board[2][0]}{board[1][1]}{board[0][2]}' == x


def solution(board):
    o = x = 0
    for b in board:
        o += b.count('O')
        x += b.count('X')

    if o < x or o > x + 1:
        return 0

    tboard = [''.join(x) for x in zip(*board)]
    win_o, win_x = check(board, tboard, 'OOO'), check(board, tboard, 'XXX')
    
    if win_o and win_x:
        return 0
    if win_o and o != x + 1:
        return 0
    if win_x and o != x:
        return 0
    return 1
