from collections import Counter


def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    l1, l2 = [], []
    for i in range(len(str1) - 1):
        check = str1[i] + str1[i + 1]
        if check.isalpha():
            l1.append(check)
    for i in range(len(str2) - 1):
        check = str2[i] + str2[i + 1]
        if check.isalpha():
            l2.append(check)

    cnt1, cnt2 = Counter(l1), Counter(l2)
    intersection = list((cnt1 & cnt2).elements())
    union = list((cnt1 | cnt2).elements())

    if not len(union) and not len(intersection):
        answer = 1
    else:
        answer = len(intersection) / len(union)

    return int(answer * 65536)