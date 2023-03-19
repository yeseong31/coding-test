def solution(citations):
    for i, v in enumerate(sorted(citations, reverse=True)):
        if i >= v:
            return i
    return len(citations)