def solution(scores):
    answer = scores[0]
    scores.sort(key=lambda x: (-x[0], x[1]))
    _max, rank = 0, 1
    
    for w, p in scores:
        if answer[0] < w and answer[1] < p:
            return -1
        if _max > p:
            continue
        if sum(answer) < w + p:
            rank += 1
        _max = p
            
    return rank
