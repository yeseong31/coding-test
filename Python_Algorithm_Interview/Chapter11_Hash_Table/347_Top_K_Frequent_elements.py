# 상위 K 빈도 요소(307p)
# k번 이상 등장하는 요소를 추출하라
from collections import Counter
import heapq


def topKFrequent(nums: list[int], k: int) -> list[int]:
    cnt = Counter(nums)
    q = []
    for c in cnt:
        heapq.heappush(q, (-cnt[c], c))

    res = []
    for _ in range(k):
        res.append(heapq.heappop(q)[1])

    return res


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(topKFrequent(nums, k))

nums = [1, 2]
k = 2
print(topKFrequent(nums, k))

