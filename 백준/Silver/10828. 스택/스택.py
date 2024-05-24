import sys
input = sys.stdin.readline

n = int(input())

stack = []
for _ in range(n):
    command = input().split()
    if command[0] == 'push':
        stack.append(int(command[1]))
    elif command[0] == 'top':
        print(stack[-1] if stack else -1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        print(1 if len(stack) == 0 else 0)
    else:
        print(stack.pop(-1) if stack else -1)