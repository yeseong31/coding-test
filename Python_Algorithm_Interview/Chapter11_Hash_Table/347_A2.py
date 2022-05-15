# 풀이 2 - 파이썬다운 방식
from collections import Counter


def topKFrequent(nums: list[int], k: int) -> list[int]:
    return list(zip(*Counter(nums).most_common(k)))[0]


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(Counter(nums).most_common(k))

print(list(zip(*Counter(nums).most_common(k))))

print(list(zip(Counter(nums).most_common(k))))
