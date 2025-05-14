def solution(progresses, speeds):
    answer = []
    days = 0
    current = 0
    
    while True:
        days += 1
        if current == len(progresses):
            break
            
        count = 0
        while current < len(progresses) and progresses[current] + speeds[current] * days >= 100:
            current += 1
            count += 1
    
        if count > 0:
            answer.append(count)
    
    return answer
