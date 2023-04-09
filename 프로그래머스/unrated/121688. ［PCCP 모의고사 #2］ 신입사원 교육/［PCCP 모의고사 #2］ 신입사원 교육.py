from heapq import heapify, heappush, heappop


def solution(ability, number):
    heapify(ability)
    for _ in range(number):
        n = heappop(ability) + heappop(ability)
        heappush(ability, n)
        heappush(ability, n)
    return sum(ability)