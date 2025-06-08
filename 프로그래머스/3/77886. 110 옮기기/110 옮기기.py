def count(x):
    res = 0
    stack = []

    for c in x:
        if c != '0' or stack[-2:] != ['1', '1']:
            stack.append(c)
            continue

        del stack[-2:]
        res += 1

    return ''.join(stack), res


def solution(s):    
    answer = []
    
    for target in s:
        trans, cnt = count(target)
        
        check = False
        for i in range(len(trans) - 1, -1, -1):
            if trans[i] == '0':
                answer.append(trans[:i+1] + '110' * cnt + trans[i+1:])
                check = True
                break
        
        if not check:
            answer.append('110' * cnt + trans)
    
    return answer
