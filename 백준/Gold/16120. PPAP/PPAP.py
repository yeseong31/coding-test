s = input()
n = len(s)
stack = []

i = 0
while i < n:
    stack.append(s[i])
    while ''.join(stack[-4:]) == 'PPAP':
        for _ in range(4):
            stack.pop()
        stack.append('P')
    i += 1
if ''.join(stack) == 'P':
    print('PPAP')
else:
    print('NP')