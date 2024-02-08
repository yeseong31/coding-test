def solution(cards):
    answer = []
    visited = [False] * len(cards)
    
    for i in range(len(cards)):
        if not visited[i]:
            visited[i] = True
            cnt = 1
            t = i
            
            while not visited[cards[t] - 1]:
                cnt += 1
                t = cards[t] - 1
                visited[t] = True
            
            answer.append(cnt)
    
    if len(answer) == 1:
        return 0
    
    answer.sort(reverse=True)
    return answer[0] * answer[1]
