def solution(citations):
    citations.sort(reverse=True)
    return sum(i < v for i, v in enumerate(citations))