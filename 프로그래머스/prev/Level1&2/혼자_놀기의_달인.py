def solution(cards):
    answer = []
    n = len(cards)
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            cnt, t = 1, i
            while not visited[cards[t] - 1]:
                cnt += 1
                t = cards[t] - 1
                visited[t] = True
            answer.append(cnt)

    if len(answer) == 1:
        return 0
    answer.sort(reverse=True)
    return answer[0] * answer[1]
