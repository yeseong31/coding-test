from itertools import combinations


def solution(n):
    answer = []
    target = '9876543210'
    for i in range(1, 11):
        if len(answer) > n:
            break
        tmp = []
        for comb in list(combinations(target, i)):
            tmp.append(int(''.join(comb)))
        answer.extend(tmp)
    answer.sort()
    if len(answer) <= n:
        return -1
    return answer[n]


print(solution(int(input())))