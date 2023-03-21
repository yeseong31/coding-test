def solution(triangle):
    for i in range(len(triangle) - 1, 0, -1):
        for j in range(1, i + 1):
            if triangle[i][j - 1] <= triangle[i][j]:
                triangle[i - 1][j - 1] += triangle[i][j]
            else:
                triangle[i - 1][j - 1] += triangle[i][j - 1]
    return triangle[0][0]