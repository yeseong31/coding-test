from collections import deque


def solution(bridge_length, weight, truck_weights):
    t = 0
    seq = 0
    current = 0
    
    q = deque()
    
    while seq != len(truck_weights):
        t += 1
        if q and q[0][1] == t:
            current -= truck_weights[q.popleft()[0]]
        
        if current + truck_weights[seq] <= weight:
            q.append((seq, t + bridge_length))
            current += truck_weights[seq]
            seq += 1
            
    while q:
        t += 1
        if q[0][1] == t:
            q.popleft()
    
    return t