s = input()
bomb = input()
i, n, m = 0, len(s), len(bomb)
stack = []
while i < n:
    stack.append(s[i])
    while ''.join(stack[-m:]) == bomb:
        for _ in range(m):
            stack.pop()
    i += 1

if not stack:
    print('FRULA')
else:
    print(''.join(stack))