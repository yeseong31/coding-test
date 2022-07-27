def solution(A: list, B: list):
    return sum(x * y for x, y in zip(sorted(A), sorted(B, reverse=True)))
