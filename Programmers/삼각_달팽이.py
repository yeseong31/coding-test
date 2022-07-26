def solution(n):
    answer = []

    board = [[0] * n for _ in range(n)]
    # 0. 초기 기준점 세팅
    cnt = 1
    i, j = 0, 0
    step = n
    cycle = 0

    while step >= 0:
        if board[i][j] == 0:
            board[i][j] = cnt
        # 1. 기준점에서부터 아래로 채우기
        for a in range(i + 1, n - cycle):
            cnt += 1
            board[a][j] = cnt
        # 2. 오른쪽으로 채우기
        for b in range(j + 1, n - (2 * cycle)):
            cnt += 1
            board[-1 - cycle][b] = cnt
        # 3. 좌상향으로 채우기
        x, y = n - 2 - cycle, n - 2 - (2 * cycle)
        for c in range(step - 2):
            cnt += 1
            board[x][y] = cnt
            x, y = x - 1, y - 1
        # 4. 기준점 다시 세팅
        i += 2
        j += 1
        step -= 3
        cnt += 1
        cycle += 1

    for i in range(n):
        for j in range(n):
            answer.append(board[i][j])
            if i == j:
                break

    return answer


print(solution(6))
