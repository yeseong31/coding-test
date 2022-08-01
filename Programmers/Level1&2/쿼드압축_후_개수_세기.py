def solution(arr):
    # k 크기의 영역을 확인
    def check_area(i, j, s, value):
        for a in range(i, i + s):
            for b in range(j, j + s):
                if arr[a][b] != value:
                    return False
        return True

    def check_visit(i, j):
        for a in range(i, i + k):
            for b in range(j, j + k):
                visited[a][b] = True

    answer = [0, 0]
    n = len(arr)

    # 모든 원소가 0 또는 1일 때
    if check_area(0, 0, n, 0):
        return [1, 0]
    elif check_area(0, 0, n, 1):
        return [0, 1]

    k = n // 2
    visited = [[False] * n for _ in range(n)]

    while k > 0:
        for x in range(0, n, k):
            for y in range(0, n, k):
                # 이미 처리가 완료된 영역은 확인하지 않음
                if visited[x][y]:
                    continue
                # 영역 확인 및 방문 처리
                if check_area(x, y, k, arr[x][y]):
                    check_visit(x, y)
                    answer[arr[x][y]] += 1
        k //= 2

    return answer


arr = [[0,0],[0,0]]
print(solution(arr))
