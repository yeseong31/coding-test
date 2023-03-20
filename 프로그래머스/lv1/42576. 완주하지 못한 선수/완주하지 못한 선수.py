def solution(participant, completion):
    answer, v = {}, 0
    for p in participant:
        answer[hash(p)] = p
        v += int(hash(p))
    for c in completion:
        v -= int(hash(c))
    return answer[v]