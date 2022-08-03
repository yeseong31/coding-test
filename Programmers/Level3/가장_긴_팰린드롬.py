def solution(s):
    # 팰린드롬 확인
    def check(left, right):
        while 0 <= left and right <= len(s) and s[left] == s[right - 1]:
            left -= 1
            right += 1
        return s[left+1:right-1]

    if len(s) <= 1:
        return len(s)

    answer = ''
    for i in range(len(s) - 1):
        answer = max(answer, check(i, i + 1), check(i, i + 2), key=lambda x: len(x))
    return len(answer)


s = "abcdcba"
print(solution(s))
