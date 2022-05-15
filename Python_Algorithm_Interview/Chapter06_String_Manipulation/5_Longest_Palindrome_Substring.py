# 가장 긴 팰린드롬 부분 문자열(159p)


def longestPalindrome(s: str) -> str:
    # 팰린드롬 문자열 판별 및 투 포인터 확장
    def expand(left: int, right: int) -> str:
        while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
            left -= 1
            right += 1
        return s[left + 1:right - 1]

    # 문자열의 길이가 두 글자 미만이거나 그 자체로 팰린드롬 문자열이라면 그대로 반환
    if len(s) < 2 or s[:] == s[::-1]:
        return s

    result = ''
    for i in range(len(s) - 1):
        # 홀수와 짝수의 경우를 나누어서 생각해야 함
        result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)
    return result


s = "babad"
print(longestPalindrome(s))
