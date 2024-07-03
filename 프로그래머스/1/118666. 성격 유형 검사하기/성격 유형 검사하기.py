from collections import defaultdict


def solution(survey, choices):
    indicators = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
    dic = defaultdict(int)

    for s, c in zip(survey, choices):
        c -= 4
        if c < 0:
            dic[s[0]] += abs(c)
        elif c > 0:
            dic[s[1]] += c

    return ''.join(a if dic[a] >= dic[b] else b for a, b in indicators)
