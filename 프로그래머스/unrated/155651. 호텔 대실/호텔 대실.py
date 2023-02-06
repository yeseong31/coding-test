from heapq import heappush, heappop


def solution(book_time):
    answer = 1
    q = []
    
    for start, end in sorted([(int(s[:2]) * 60 + int(s[3:]), int(e[:2]) * 60 + int(e[3:])) for s, e in book_time]):
        if not q:
            heappush(q, end)
            continue
            
        if q[0] <= start:
            heappop(q)
        else:
            answer += 1
            
        heappush(q, end + 10)
        
    return answer