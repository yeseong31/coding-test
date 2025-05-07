def solution(strings, n):
    return [s for s in sorted(strings, key=lambda x: (x[n], x))]