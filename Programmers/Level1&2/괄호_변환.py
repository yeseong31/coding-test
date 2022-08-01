def solution(p):
    dic = {
        '(': ')',
        ')': '('
    }

    # 문자열 뒤집음
    def reverse_str(s):
        result = ''
        for c in s:
            result += dic[c]
        return result

    # 올바른 괄호 문자열 판단
    def check(s):
        stack = []
        for c in s:
            if stack and c == ')' and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(c)
        if not stack:
            return True
        return False

    def balanced_str(s):
        idx = 0
        balance = 0
        lst = []

        for c in s:
            if c == '(':
                balance += 1
            else:
                balance -= 1
            lst.append(c)
            idx += 1
            if balance == 0:
                break

        return idx

    # 1. 빈 문자열이라면, 빈 문자열 반환
    if len(p) == 0:
        return p

    # 2. 문자열 p를 '균형잡힌 괄호 문자열' u, v로 분리
    i = balanced_str(p)
    u, v = ''.join(p[:i]), ''.join(p[i:])

    # 3. 올바른 괄호 문자열 판단
    if check(u):
        return u + solution(v)
    else:
        return '(' + solution(v) + ')' + reverse_str(u[1:-1])