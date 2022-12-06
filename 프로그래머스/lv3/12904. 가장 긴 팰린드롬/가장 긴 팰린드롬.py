def solution(s):
    def check(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1
    
    if len(s) == 1:
        return 1
    return max(max(check(i, i + 1), check(i, i + 2)) for i in range(len(s) - 1))