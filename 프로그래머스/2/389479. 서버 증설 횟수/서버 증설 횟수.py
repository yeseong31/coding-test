from heapq import heappush, heappop


def solution(players, m, k):
    answer = 0
    q = []
    
    heappush(q, 24)
    
    for t, p in enumerate(players):
        while q and q[0] == t:
            heappop(q)
        
        if p < len(q) * m:
            continue
    
        while len(q) * m <= p:
            heappush(q, t + k)
            answer += 1
    
    return answer
