def solution(places):
    dx, dy = (0, 1, 1, 1, 0, -1, -1, -1), (1, 1, 0, -1, -1, -1, 0, 1)
    
    def check(board):
        for x in range(5):
            for y in range(5):
                if board[x][y] != 'P':
                    continue
                for k in range(8):
                    nx, ny = x + dx[k], y + dy[k]
                    # 영역 밖이라면 확인하지 않음
                    if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                        continue
                    # 대각선 확인
                    if k % 2 == 1:
                        # 사이에 빈 테이블이 있는 경우 
                        if board[nx][ny] == 'P' and (board[x][ny] == 'O' or board[nx][y] == 'O'):
                            return 0
                    # 상하좌우 - 맨해튼 거리 1 확인
                    elif board[nx][ny] == 'P':
                        return 0
                    # 상하좌우 - 맨해튼 거리 2 확인
                    elif board[nx][ny] == 'O':
                        nx, ny = nx + dx[k], ny + dy[k]
                        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                            continue
                        if board[nx][ny] == 'P':
                            return 0
        return 1
    
    return [check(place) for place in places]
