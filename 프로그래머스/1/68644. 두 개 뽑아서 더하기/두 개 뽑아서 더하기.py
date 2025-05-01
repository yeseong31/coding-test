from itertools import combinations


def solution(numbers):
    answer = set(sum(x) for x in combinations(numbers, 2))
    return sorted(list(answer))
    