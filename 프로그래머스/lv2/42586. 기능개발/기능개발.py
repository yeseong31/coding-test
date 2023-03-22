from math import ceil


def solution(progresses, speeds):
    answer = []
    stack = []
    
    cnt = 0
    for day in [ceil((100 - p) / s) for p, s in zip(progresses, speeds)]:
        while stack and stack[0] < day:
            stack.pop()
            cnt += 1
        stack.append(day)
        if cnt > 0:
            answer.append(cnt)
            cnt = 0
    
    return answer + [len(stack)]
