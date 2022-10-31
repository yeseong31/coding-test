def solution(n, results):
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    for x, y in results:
        graph[x][y] = 1

    # 승리 횟수 확인
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                if graph[a][k] == graph[k][b] == 1:
                    graph[a][b] = 1

    # (승리 + 패배)가 n - 1인 경우 정답
    answer = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j]:
                answer[i] += 1
                answer[j] += 1

    return answer.count(n - 1)


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
