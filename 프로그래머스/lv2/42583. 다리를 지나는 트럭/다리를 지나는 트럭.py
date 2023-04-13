from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    check = idx = cur_weight = 0
    q = deque()
    
    while check < len(truck_weights):
        if q and answer - q[0][1] == bridge_length:
            cur_weight -= q.popleft()[0]
            check += 1
        if idx < len(truck_weights) and cur_weight + truck_weights[idx] <= weight:
            q.append((truck_weights[idx], answer))
            cur_weight += truck_weights[idx]
            idx += 1
        answer += 1
    
    return answer
