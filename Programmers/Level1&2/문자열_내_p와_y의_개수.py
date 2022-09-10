from collections import Counter


def solution(s):
    s = s.lower()
    cnt = Counter(s)
    return cnt['p'] == cnt['y']


s = "pPoooyY"
print(solution(s))
