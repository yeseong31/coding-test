import sys

# 문자열(스택)
s1 = list(sys.stdin.readline().rstrip())
s2 = []

# 명령어의 수
m = int(sys.stdin.readline())

for _ in range(m):
    # 입력된 명령어
    c = sys.stdin.readline().split()
    
    if c[0] == 'L':
        if s1:
            s2.append(s1.pop())
    elif c[0] == 'D':
        if s2:
            s1.append(s2.pop())
    elif c[0] == 'B':
        # 삭제할 문자가 있는 경우에만 삭제
        if s1:
            s1.pop()
    elif c[0] == 'P':
        s1.append(c[1])

s1.extend(s2[::-1])
print(''.join(s1))
