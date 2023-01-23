s = input()
t = list(input())

answer = 0
while len(t) > len(s):
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t.reverse()

if s == ''.join(t):
    print(1)
else:
    print(0)