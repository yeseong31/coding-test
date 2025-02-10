def solution(x):
    return not x % sum(map(int, str(x)))