def solution(brown, yellow):
    for n in range(3, int((brown + yellow) ** 0.5) + 1):
        div, mod = divmod(brown + yellow, n)
        if mod != 0 or (n - 2) * (div - 2) != yellow:
            continue
        return div, n