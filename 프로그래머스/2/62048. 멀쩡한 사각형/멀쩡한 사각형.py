import math


def solution(w,h):
    n = math.gcd(w, h)
    return w * h - ((w // n) + (h // n) - 1) * n
