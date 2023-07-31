from collections import defaultdict


def solution(n, results):
    answer = 0
    win, lose = defaultdict(set), defaultdict(set)
    
    for a, b in results:
        win[a].add(b)
        lose[b].add(a)
    
    # A 선수는 B 선수를 항상 이김 
    for i in range(1, n + 1):
        for w in win[i]:
            lose[w].update(lose[i])
        for l in lose[i]:
            win[l].update(win[i])
    
    # 이긴 경기의 수와 진 경기의 수를 합했을 때 n - 1이 나와야 함
    for i in range(1, n + 1):
        if len(win[i]) + len(lose[i]) == n - 1:
            answer += 1
    return answer