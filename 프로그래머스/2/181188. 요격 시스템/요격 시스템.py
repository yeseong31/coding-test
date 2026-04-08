def solution(targets):
    answer = 0
    n = len(targets)

    targets.sort(key=lambda x: x[0])

    idx = n - 1

    while idx >= 0:
        start = targets[idx][0]

        while idx >= 0 and start < targets[idx][1]:
            idx -= 1

        answer += 1

    return answer