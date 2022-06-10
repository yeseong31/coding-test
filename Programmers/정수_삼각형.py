def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(i + 1):
            # 현재 위치에서 왼쪽 위 확인 (↖)
            left = 0 if j == 0 else triangle[i - 1][j - 1]
            # 현재 위치에서 오른쪽 위 확인 (↗)
            right = 0 if j == i else triangle[i - 1][j]
            # 비교 수행
            triangle[i][j] += max(left, right)

    # 거쳐간 숫자의 최댓값
    return max(triangle[len(triangle) - 1])