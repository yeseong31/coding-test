def solution(s):
    answer = ''
    prev = True
    for c in s.lower():
        print(c)
        # 공백인 경우
        if c == ' ':
            prev = True
        # 숫자인 경우
        elif c.isdigit():
            prev = False
        # 첫 글자인 경우
        elif prev:
            answer += c.upper()
            prev = False
            continue
        answer += c

    return answer


print(solution("3people unFollowed me"))
