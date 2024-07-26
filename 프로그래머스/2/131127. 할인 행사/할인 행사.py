from collections import Counter


def solution(want, number, discount):
    dic = {v: number[i] for i, v in enumerate(want)}
    return sum(dic == Counter(discount[i:i + 10]) for i in range(len(discount) - 9))
