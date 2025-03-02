stack = ['(']
prev = '('
result = 0

for c in input()[1:]:
    # '('라면 스택에 추가
    if c == '(':
        stack.append(c)
    # ')'라면
    else:
        stack.pop()
        # 직전의 문자가 '('인 경우 레이저로 막대기를 자름
        if prev == '(':
            result += len(stack)
        # 그렇지 않으면 막대기를 하나 제거
        else:
            result += 1
    prev = c

print(result)