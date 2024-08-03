from collections import defaultdict

def solution(N, stages):
    result = []
    length = len(stages)

    for i in range(1, N + 1):
        cnt = stages.count(i)
        result.append((i, cnt) if length <= 0 else (i, cnt / length))
        length -= cnt
    
    answer = sorted(result, key=lambda x: x[1], reverse=True)
    return [x[0] for x in answer]    
    