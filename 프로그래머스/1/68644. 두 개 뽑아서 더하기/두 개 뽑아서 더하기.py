from itertools import combinations


def solution(numbers):
    numbers = set(map(sum ,combinations(numbers, 2)))
    return sorted(numbers)