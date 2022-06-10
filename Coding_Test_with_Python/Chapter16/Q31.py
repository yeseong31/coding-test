"""
Q31 금광(375p)
"""

dy = [-1, 0, 1]

# 테스트 케이스만큼 반복
for _ in range(int(input())):
    n, m = map(int, input().split())
    board = list(map(int, input().split()))

    # dp 테이블
    d = []
    idx = 0
    for i in range(n):
        d.append(board[idx:idx + m])
        idx += m

    # 다이나믹 프로그래밍
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 상단
            top = 0 if i == 0 else d[i - 1][j - 1]
            # 왼쪽 하단
            down = 0 if i == n - 1 else d[i + 1][j - 1]
            # 왼쪽 중앙
            mid = d[i][j - 1]

            # 값 비교
            d[i][j] += max(top, down, mid)

    result = 0
    for x in range(n):
        result = max(result, d[x][-1])
    print(result)
