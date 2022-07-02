# 가장 긴 팰린드롬 부분 문자열(159p)


def longestPalindrome(s: str) -> str:

    def check_palindrome(left: int, right: int) -> str:
        while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
            left -= 1
            right += 1
        return s[left + 1:right - 1]

    # 문자열의 길이가 2 미만이거나 s 자체가 팰린드롬이라면 s 반환
    if len(s) < 2 or s == s[::-1]:
        return s

    target = ''
    for i in range(len(s) - 1):
        target = max(target, check_palindrome(i, i + 1), check_palindrome(i, i + 2))

    return target


s = "babad"
print(longestPalindrome(s))
