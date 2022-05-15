"""
괄호 변환 (346p)
"""


# 올바른 괄호 문자열 판단
def check(lst):
    stack = []
    for c in lst:
        if c == ')' and stack and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(c)

    if not stack:
        return True
    return False


# 문자열 뒤집기
def reverse_parenthesis(s):
    result = []
    dic = {
        '(': ')',
        ')': '('
    }

    for c in s:
        result.append(dic[c])

    return ''.join(result)


# 입력으로 들어오는 문자열 p는 항상 '균형잡힌 괄호 문자열'
def solution(p):
    # 빈 문자열인 경우, 빈 문자열 반환
    if p == '':
        return p

    # 균형잡힌 괄호 문자열 판단 → '('을 만나면 -1, ')'을 만나면 +1
    balanced = 0

    # 문자열 p를 두 '균형잡힌 괄호 문자열' u, v로 분리
    u = []
    for c in p:
        if c == '(':
            balanced -= 1
        else:
            balanced += 1
        u.append(c)
        if balanced == 0:
            break

    v = ''.join(list(p)[len(u):])

    if check(u):
        return ''.join(u) + solution(v)
    else:
        return '(' + solution(v) + ')' + reverse_parenthesis(u[1:-1])


for p in ['', '(()())()', ')(', '()))((()']:
    print(solution(p))
