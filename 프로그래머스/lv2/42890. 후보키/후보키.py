from itertools import combinations


def solution(relation):
    row = len(relation)
    col = len(relation[0])

    comb = []
    for i in range(1, col + 1):
        comb.extend(combinations(range(col), i))

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

        for u in unique:
            if set(u).issubset(set(num)):
                flag = False
                break
        if flag:
            unique.append(num)

    return len(unique)