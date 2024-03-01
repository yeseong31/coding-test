from collections import deque


def solution(numbers, target):
    answer = 0
    q = deque([(0, 0)])
    
    while q:
        index, result = q.popleft()
        
        if index == len(numbers):
            if result == target:
                answer += 1
            continue
        
        q.append((index + 1, result + numbers[index]))
        q.append((index + 1, result - numbers[index]))
    
    return answer