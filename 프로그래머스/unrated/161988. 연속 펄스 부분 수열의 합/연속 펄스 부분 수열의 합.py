def solution(sequence):
    answer = -1
    s1, s2, p = 0, 0, 1
    for i, v in enumerate(sequence):
        s1 = s1 + v * p if s1 >= v * -p else 0
        s2 = s2 + v * -p if s2 >= v * p else 0
        answer = max(answer, s1, s2)
        p *= -1
    return answer
