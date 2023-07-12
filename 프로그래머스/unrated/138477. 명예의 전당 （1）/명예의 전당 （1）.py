from heapq import heappush, heappop


def solution(k, score):
    answer = []
    q = []
    
    for s in score:
        heappush(q, s)
        if len(q) > k:
            heappop(q)
        answer.append(q[0])
    
    return answer