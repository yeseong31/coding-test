from itertools import combinations


def solution(numbers):
    answer = []

    for a, b in list(combinations(sorted(numbers), 2)):
        answer.append(a + b)

    return sorted(list(set(answer)))