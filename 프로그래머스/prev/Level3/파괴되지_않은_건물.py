def solution(board, skill):
    n, m = len(board), len(board[0])
    check = [[0] * (m + 1) for _ in range(n + 1)]

    # 파괴 및 회복 구간 확인
    for _type, r1, c1, r2, c2, degree in skill:
        if _type == 1:
            degree *= -1
        check[r1][c1] += degree
        check[r2 + 1][c2 + 1] += degree
        check[r2 + 1][c1] -= degree
        check[r1][c2 + 1] -= degree

    # 구간 합: 행
    for i in range(1, n + 1):
        for j in range(m + 1):
            check[i][j] += check[i - 1][j]

    # 구간 합: 열
    for j in range(1, m + 1):
        for i in range(n + 1):
            check[i][j] += check[i][j - 1]

    # 결과 확인
    answer = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] + check[i][j] > 0:
                answer += 1
    return answer


print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]], [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))
