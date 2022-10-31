"""
후보키
https://school.programmers.co.kr/learn/courses/30/lessons/42890
"""
from itertools import combinations


def solution(relation):
    row = len(relation)
    col = len(relation[0])

    comb = []
    for i in range(1, col + 1):
        comb.extend(combinations(range(col), i))

    # 유일성
    unique = []
    for num in comb:
        res = []
        flag = False

        for i in num:
            tmp = []
            for rel in relation:
                for j, r in enumerate(rel):
                    if i == j:
                        tmp.append(r)
            res.append(tmp)

        check = set()
        for target in zip(*res):
            if target not in check:
                check.add(target)
        if len(check) == row:
            flag = True

        # 최소성
        for u in unique:
            if set(u).issubset(set(num)):
                flag = False
                break
        if flag:
            unique.append(num)

    return len(unique)


relation = [["100", "ryan", "music", "2"],
            ["200", "apeach", "math", "2"],
            ["300", "tube", "computer", "3"],
            ["400", "con", "computer", "4"],
            ["500", "muzi", "music", "3"],
            ["600", "apeach", "music", "2"]]
print(solution(relation))
