def solution(s):
    def check(target):
        stack = []

        for t in target:
            if t in ['(', '[', '{']:
                stack.append(t)
            else:
                if not stack:
                    return False
                if stack.pop() != dic[t]:
                    return False

        if stack:
            return False
        return True

    dic = {
        '}': '{',
        ')': '(',
        ']': '['
    }

    cnt = 0

    for i in range(len(s)):
        left, right = s[:i], s[i:]
        if check(right + left):
            cnt += 1

    return cnt

print(solution("}}}"))

