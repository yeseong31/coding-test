# 풀이 1 - Counter를 이용한 음수 순 추출
import heapq
from collections import Counter


def topKFrequent(nums: list[int], k: int) -> list[int]:
    count = Counter(nums)
    q = []
    res = []

    for c in count:
        heapq.heappush(q, (-count[c], c))

    for _ in range(k):
        res.append(heapq.heappop(q)[1])

    return res
