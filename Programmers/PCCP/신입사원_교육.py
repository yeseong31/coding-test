import heapq


def solution(ability, number):
    heapq.heapify(ability)

    for _ in range(number):
        target = heapq.heappop(ability) + heapq.heappop(ability)
        heapq.heappush(ability, target)
        heapq.heappush(ability, target)

    return sum(ability)
