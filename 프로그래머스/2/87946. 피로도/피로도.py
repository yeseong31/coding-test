from itertools import permutations


def solution(k, dungeons):
    answer = -1

    for check in permutations(range(len(dungeons))):
        count = 0
        current_k = k

        for seq in check:
            condition, cost = dungeons[seq]
            
            if current_k < condition:
                break
                
            current_k -= cost
            count += 1

        answer = max(answer, count)

    return answer
