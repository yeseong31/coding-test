from collections import deque


def solution(numbers, target):
    answer = 0
    q = deque([(0, 0)])
    
    while q:
        n, i = q.popleft()
        if i == len(numbers):
            if n == target:
                answer += 1
            continue
        q.append((n + numbers[i], i + 1))
        q.append((n - numbers[i], i + 1))
    
    return answer