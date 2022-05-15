"""
실패울 (361p)
"""


def solution(N, stages):
    result = []
    length = len(stages)

    for i in range(1, N + 1):
        cnt = stages.count(i)

        # value: 실패율
        if length == 0:
            v = 0
        else:
            v = cnt / length

        result.append((i, v))
        length -= cnt

    return [i for i, _ in sorted(result, key=lambda x: x[1], reverse=True)]


# 스테이지의 수
n = 5
# 플레이어가 멈춰있는 스테이지의 번호
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(n, stages))
