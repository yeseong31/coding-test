def solution(s):
    def check(target):
        stack = []
        for t in target:
            if t in ['(', '[', '{']:
                stack.append(t)
            elif not stack or stack.pop() != dic[t]:
                return False
        return not stack

    dic = {
        '}': '{',
        ')': '(',
        ']': '['
    }

    return sum(check(s[i:] + s[:i]) for i in range(len(s)))