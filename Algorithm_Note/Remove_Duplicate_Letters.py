# 중복 문자 제거
# 중복된 문자를 제외하고 사전식 순서로 나열하라.

# 풀이 1 - 재귀를 이용한 분리
from collections import Counter


def removeDuplicateLetters(s: str) -> str:
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

# -----------------------------------------------------------------------------
# 풀이 2 - 스택을 이용한 문자 제거


def removeDuplicateLetters(s: str) -> str:
    counter, seen, stack = Counter(s), set(), []

    for c in s:
        counter[c] -= 1
        if c in seen:
            continue
        # 뒤에 붙일 문자가 남아 있다면 스택에서 제거
        while stack and c < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack.pop())
        stack.append(c)
        seen.add(c)

    return ''.join(stack)


s = "bcabc"
print(removeDuplicateLetters(s))

s = "cbacdcbc"
print(removeDuplicateLetters(s))

s = "cdadabcc"
print(removeDuplicateLetters(s))
