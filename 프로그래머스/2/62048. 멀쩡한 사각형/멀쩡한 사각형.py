from math import gcd


def solution(w,h):
    n = gcd(w, h)
    return w * h - ((w + h - n) // n) * n
