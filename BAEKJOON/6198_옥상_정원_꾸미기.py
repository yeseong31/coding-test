n = int(input())
height = [int(input()) for _ in range(n)]
stack = []
checked = 0
for h in height:
    while stack and stack[-1] <= h:
        stack.pop()
    stack.append(h)
    checked += len(stack) - 1
print(checked)
