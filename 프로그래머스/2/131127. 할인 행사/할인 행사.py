from collections import Counter


def solution(want, number, discount):
    answer = 0
    dic = {v: number[i] for i, v in enumerate(want)}
    
    for i in range(len(discount) - 9):
        answer += dic == Counter(discount[i:i + 10])
    
    return answer
