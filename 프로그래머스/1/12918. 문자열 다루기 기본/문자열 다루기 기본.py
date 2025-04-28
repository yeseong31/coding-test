from re import match


def solution(s):
    return bool(match('\d{4}$|\d{6}$', s))