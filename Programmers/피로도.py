# 탐험 시작을 위한 '최소 필요 피로도' start
# 탐험을 마쳤을 때 소모되는 '소모 피로도' end

# 현재 피로도 k
import itertools


def solution(k, dungeons):
    answer = -1

    for check in list(itertools.permutations(range(len(dungeons)))):
        cnt = 0
        now_k = k

        for i in check:
            cond, cost = dungeons[i]
            if now_k < cond:
                break
            now_k -= cost
            cnt += 1

        answer = max(answer, cnt)

    return answer


k = 80
dungeons = [[80,20],[50,40],[30,10]]
print(solution(k, dungeons))
