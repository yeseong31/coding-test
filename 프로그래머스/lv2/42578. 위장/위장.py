from collections import defaultdict


def solution(clothes):
    answer = 1
    dic = defaultdict(int)
    for name, types in clothes:
        dic[types] += 1
    for v in dic.values():
        answer *= (v + 1)
    return answer - 1
