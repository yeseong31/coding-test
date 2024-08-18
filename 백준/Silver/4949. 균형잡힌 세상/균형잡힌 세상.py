while True:
    s = input()
    if s == '.':
        break
    stack = []
    check = True
    for c in s:
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')':
            if not stack or stack.pop() != '(':
                check = False
                break
        elif c == ']':
            if not stack or stack.pop() != '[':
                check = False
                break
    if check and not stack:
        print('yes')
    else:
        print('no')
