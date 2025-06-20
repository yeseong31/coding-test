def solution(s):
    target = list(map(int, s.split()))
    return f'{min(target)} {max(target)}'