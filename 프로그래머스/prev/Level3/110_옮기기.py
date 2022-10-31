def solution(s):
    def count(x):
        res = 0
        stack = []
        for c in x:
            if c == '0' and stack[-2:] == ['1', '1']:
                del stack[-2:]
                res += 1
            else:
                stack.append(c)
        return ''.join(stack), res

    answer = []
    for target in s:
        trans, cnt = count(target)
        # '0' 뒤에 '110' 뭉치를 붙임
        for i in range(len(trans) - 1, -1, -1):
            if trans[i] == '0':
                answer.append(trans[:i+1] + '110' * cnt + trans[i+1:])
                break
        else:
            answer.append('110' * cnt + trans)
    return answer


s = ["1110","100111100","0111111010"]
print(solution(s))
