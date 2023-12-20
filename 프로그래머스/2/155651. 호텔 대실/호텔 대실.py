from heapq import heappush, heappop


def calculate_time(s, e):
    return int(s[:2]) * 60 + int(s[3:]), int(e[:2]) * 60 + int(e[3:])


def solution(book_time):
    answer = 1
    q = []
    
    reservations = [(calculate_time(s, e)) for s, e in book_time]
    
    for s, e in sorted(reservations):
        if not q:
            heappush(q, e)
            continue
            
        if q[0] <= s:
            heappop(q)
        else:
            answer += 1
            
        heappush(q, e + 10)
        
    return answer
