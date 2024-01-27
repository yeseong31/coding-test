def solution(name, yearning, photo):
    s = {n: s for n, s in zip(name, yearning)}
    return [sum(s[v] for v in p if v in s) for p in photo]
