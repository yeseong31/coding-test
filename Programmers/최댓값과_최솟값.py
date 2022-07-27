def solution(s):
    target = list(map(int, s.split()))
    return f'{min(target)} {max(target)}'


s = '1 2 3 4'
print(solution(s))
