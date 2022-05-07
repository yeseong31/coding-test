import collections

def solution(clothes):
    dic = collections.defaultdict(int)

    for c in clothes:
        dic[c[1]] += 1

    cnt = 1
    for i in dic.values():
        cnt *= (i + 1)
    return cnt - 1