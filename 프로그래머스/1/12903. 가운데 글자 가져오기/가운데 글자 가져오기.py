def solution(s):
    index = len(s) // 2
    return s[index-1:index+1] if len(s) % 2 == 0 else s[index]
