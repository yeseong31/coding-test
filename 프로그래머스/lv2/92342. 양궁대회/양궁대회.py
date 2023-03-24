from itertools import combinations_with_replacement as cwr


def solution(n, info):
    answer = [-1]
    gap = -1

    for case in cwr(range(11), n):
        score = [0] * 11
        for i in case:
            score[10 - i] += 1

        apeach = ryan = 0
        for i in range(11):
            if info[i] == score[i] == 0:
                continue
            elif info[i] < score[i]:
                ryan += 10 - i
            else:
                apeach += 10 - i

        if apeach >= ryan:
            continue
        if ryan - apeach > gap:
            gap = ryan - apeach
            answer = score
    
    return answer