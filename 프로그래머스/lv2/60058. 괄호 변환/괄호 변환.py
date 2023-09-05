def is_valid(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif stack:
            stack.pop()
        else:
            return False
    
    return not stack


def reverse_parenthesis(s, dic):
    return ''.join(dic[c] for c in s)


def solution(p):
    dic = {
        '(': ')', ')': '('
    }
    
    if p == '':
        return p
    
    u, b = [], 0
    for c in p:
        b += 1 if c == '(' else -1
        u.append(c)
        if b == 0:
            break
    
    v = ''.join(p[len(u):])
    if is_valid(u):
        return f"{''.join(u)}{solution(v)}"
    else:
        return f'({solution(v)}){reverse_parenthesis(u[1:-1], dic)}'
