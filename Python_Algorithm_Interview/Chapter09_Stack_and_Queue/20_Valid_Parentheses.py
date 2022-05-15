# 유효한 괄호(245p)
# 괄호로 된 입력값이 올바른지 판별하라.

def isValid(s: str) -> bool:
    stack = []
    dic = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for c in s:
        if c not in dic:
            stack.append(c)
        elif not stack or dic[c] != stack.pop():
            return False

    return not stack


s = "()"
print(isValid(s))

s = "()[]{}"
print(isValid(s))

s = "(]"
print(isValid(s))
