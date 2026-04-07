def solution(name, yearning, photo):
    score = dict(zip(name, yearning))
    return [sum(score.get(p, 0) for p in pic) for pic in photo]