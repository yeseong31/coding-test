import collections
import string


def solution(msg):
    answer = []

    dic = collections.defaultdict(int)
    n = 1
    for v in string.ascii_uppercase:
        dic[v] = n
        n += 1

    p, c = 0, 0
    while True:
        c += 1
        if c == len(msg):
            answer.append(dic[msg[p:]])
            return answer
        if msg[p:c+1] not in dic:
            dic[msg[p:c+1]] = n
            n += 1
            answer.append(dic[msg[p:c]])
            p = c


msg = 'TOBEORNOTTOBEORTOBEORNOT'
print(solution(msg))
