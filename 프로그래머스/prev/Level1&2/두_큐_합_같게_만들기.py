from collections import deque


def solution(queue1, queue2):
    v1, v2 = sum(queue1), sum(queue2)

    # 예외 처리: 두 큐의 합을 같게 만들 수 없을 때
    target, mod = divmod(v1 + v2, 2)
    if mod:
        return -1

    answer = 0
    q1, q2 = deque(queue1), deque(queue2)

    while q1 and q2:
        # 왼쪽 큐에 대해서만 판단
        if v1 == target:
            return answer
        elif v1 < target:
            pop = q2.popleft()
            q1.append(pop)
            v1 += pop
        else:
            v1 -= q1.popleft()
        answer += 1

    return -1


queue1 = [1, 2, 1, 2]
queue2 = [1, 10, 1, 2]
print(solution(queue1, queue2))
