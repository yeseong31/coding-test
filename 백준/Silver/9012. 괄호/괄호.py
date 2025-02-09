t = int(input())
stack = []

for _ in range(t):
    s = input()
    for c in s:
        if c == '(':
            stack.append(c)
        elif stack:
            stack.pop()
        else:
            stack.append(c)
            break
    if stack:
        print('NO')
    else:
        print('YES')
    stack.clear()