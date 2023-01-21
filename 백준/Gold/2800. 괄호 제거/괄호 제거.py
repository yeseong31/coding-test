from itertools import combinations

s = input()
answer = set()
left, right = [], []

for i, c in enumerate(s):
    if c == '(':
        left.append(i)
    elif c == ')':
        right.append((left.pop(), i))

for i in range(1, len(s) + 1):
    for j in list(combinations(right, i)):
        target = list(s)
        for k in j:
            target[k[0]] = ''
            target[k[1]] = ''
        answer.add(''.join(target))

for ans in sorted(answer):
    print(ans)