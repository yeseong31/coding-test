# 풀이 1 - 재귀를 이용한 분리

def removeDuplicateLetters(s: str) -> str:
    # 집합으로 정렬

    for char in sorted(set(s)):
        suffix = s[s.index(char):]
        if set(s) == set(suffix):
            return char + removeDuplicateLetters(suffix.replace(char, ''))
    return ''


s = "bcabc"
print(removeDuplicateLetters(s))    # Output: "abc"

s = "cbacdcbc"
print(removeDuplicateLetters(s))    # Output: "acdb"

s = "cdadabcc"
print(removeDuplicateLetters(s))