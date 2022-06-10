import sys
input = sys.stdin.readline

s = list(input().rstrip())

i = 0
p = 0

while i < len(s):
    # 태그의 시작문자라면
    if s[i] == '<':
        i += 1
        # '>'를 만날 때까지 반복
        while s[i] != '>':
            i += 1
        i += 1
    # 숫자, 알파벳이라면
    elif s[i].isalnum():
        p = i
        # 하나의 단어 범위 지정
        while i < len(s) and s[i].isalnum():
            i += 1
        tmp = s[p:i]
        s[p:i] = tmp[::-1]
    # 공백이라면
    else:
        i += 1

print(''.join(s))
