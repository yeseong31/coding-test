from collections import defaultdict
from string import ascii_uppercase


def solution(msg):
    answer = []
    dic = defaultdict(int)
    n = 1
    
    for v in ascii_uppercase:
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
