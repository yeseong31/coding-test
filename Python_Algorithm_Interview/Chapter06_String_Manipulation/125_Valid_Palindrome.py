# 유효한 팰린드롬(138p)
import re


def isPalindrome(s: str) -> bool:
    s = re.sub('[^a-z0-9]', '', s.lower())
    return s == s[::-1]


s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))

s = "race a car"
print(isPalindrome(s))
