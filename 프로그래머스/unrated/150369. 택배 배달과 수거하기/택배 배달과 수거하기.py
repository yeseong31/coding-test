from collections import deque


def solution(cap, n, deliveries, pickups):
    def check_point(target):
        q = deque()
        point = n
        sum_value = 0

        while target:
            sum_value += target.pop()
            if sum_value >= cap:
                target.append(sum_value - cap)
                q.append(point)
                
                sum_value = 0
                while target and target[-1] == 0:
                    target.pop()
                    
                point = len(target)
        
        if point != n and point >= 0:
            q.append(point)
        return q

    answer = 0
    d = check_point(deliveries)
    p = check_point(pickups)
    
    while d and p:
        answer += max(d.popleft(), p.popleft()) * 2
    while d:
        answer += d.popleft() * 2
    while p:
        answer += p.popleft() * 2

    return answer