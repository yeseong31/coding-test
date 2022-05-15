# 2차원 리스트(행렬)를 90도 회전하는 메서드

def rotate_a_matrix_by_90_degree(a):
    # 행, 열 길이 확인
    row_length = len(a)
    col_length = len(a[0])

    # 2차원 리스트 초기화
    result = [[0] * row_length for _ in range(col_length)]

    # 2중 반복문으로 swap
    for r in range(row_length):
        for c in range(col_length):
            result[c][row_length - 1 - r] = a[r][c]
            
    return result

# 2차원 리스트
a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# 결과 확인
print(rotate_a_matrix_by_90_degree(a))
