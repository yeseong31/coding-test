def solution(N, stages):
    result = []
    # 플레이어의 수
    length = len(stages)

    for i in range(1, N + 1):
        cnt = stages.count(i)

        if length == 0:
            fail = 0
        else:
            fail = cnt / length

        result.append((i, fail))
        length -= cnt

    return [i for i, _ in sorted(result, key=lambda x: x[1], reverse=True)]