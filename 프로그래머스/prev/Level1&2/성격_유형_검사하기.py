import collections


def solution(survey: list[str], choices: list[int]) -> str:
    indicators = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
    dic = collections.defaultdict(int)

    for s, c in zip(survey, choices):
        c -= 4
        if c < 0:
            dic[s[0]] += abs(c)
        elif c > 0:
            dic[s[1]] += c

    return ''.join([a if dic[a] >= dic[b] else b for a, b in indicators])


survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
print(solution(survey, choices))
