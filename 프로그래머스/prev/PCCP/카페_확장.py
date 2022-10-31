from collections import deque


def solution(menu, order, k):
    answer = 0

    target = deque()
    n = len(order)
    t = cur = i = 0

    # 소요 시간: menu[order[i]]
    while i < n:
        if target:
            cur += 1
            if target[0] == cur:
                target.popleft()
                cur = 0
        if i < n and t % k == 0:
            target.append(menu[order[i]])
            answer = max(answer, len(target))
            i += 1
        t += 1

    return answer


menu, order, k = [1, 2, 3, 4, 5], [0, 1, 2, 3], 4
print(solution(menu, order, k))
