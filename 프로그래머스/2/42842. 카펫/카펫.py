def solution(brown, yellow):
    for h in range(3, int((brown + yellow) ** 0.5 + 1)):
        if (brown + yellow) % h == 0:
            w = (brown + yellow) // h
            if w * h - (w - 2) * (h - 2) == brown:
                return [w, h]