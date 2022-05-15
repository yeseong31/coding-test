# 중복 문자 제거(247p)
from collections import Counter


def removeDuplicateLetters(s: str) -> str:
    stack = []
    cnt = Counter(s)
    seen = set()

    for char in s:
        cnt[char] -= 1
        if char in seen:
            continue
        while stack and stack[-1] > char and cnt[stack[-1]] > 0:
            seen.remove(stack.pop())
        stack.append(char)

    return ''.join(stack)


s = "bcabc"
print(removeDuplicateLetters(s))

s = "cbacdcbc"
print(removeDuplicateLetters(s))

s = "cdadabcc"
print(removeDuplicateLetters(s))
