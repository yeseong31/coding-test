def solution(d, budget):
    for i, v in enumerate(sorted(d)):
        budget -= v
        if budget < 0:
            return i
    return len(d)