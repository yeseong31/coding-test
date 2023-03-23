def reverse(u):
    result = []
    for v in u:
        if v == '(':
            result.append(')')
        else:
            result.append('(')
    return ''.join(result)


def validate(u):
    if u == '':
        return False
    
    stack = []
    for v in u:
        if v == '(':
            stack.append('(')
            continue
        while stack and stack[-1] == '(':
            stack.pop()
    return not stack


def split(w):
    count = 0
    for i in range(len(w)):
        if i != 0 and count == 0:
            return w[:i], w[i:]
        if w[i] == '(':
            count += 1
        else:
            count -= 1
    return w, ''


def dfs(w):
    if w == '':
        return w
    u, v = split(w)
    if validate(u):
        return u + dfs(v)
    return '(' + dfs(v) + ')' + reverse(u[1:-1])


def solution(p):
    return dfs(p)