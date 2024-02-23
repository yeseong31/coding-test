answer = 0
tmp = 0
s = input()
stack = []

for c in s:
    if c.isdigit():
        answer += 1
        tmp = int(c)
        continue
    if c == '(':
        stack.append((tmp, answer - 1))
        answer = 0
    else:
        k, prev = stack.pop()
        answer = k * answer + prev

print(answer)
