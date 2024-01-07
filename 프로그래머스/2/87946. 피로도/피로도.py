from itertools import permutations


def solution(k, dungeons):
    answer = -1

    for check in permutations(range(len(dungeons))):
        count = 0
        current_k = k

        for i in check:
            cond, cost = dungeons[i]
            
            if current_k < cond:
                break
            
            current_k -= cost
            count += 1

        answer = max(answer, count)

    return answer
