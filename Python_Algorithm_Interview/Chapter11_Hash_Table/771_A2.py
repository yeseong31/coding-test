# 풀이 2 - defaultdict를 이요한 비교 생략
from collections import defaultdict


def numJewelsInStones(jewels: str, stones: str) -> int:
    freqs = defaultdict(int)
    count = 0

    for s in stones:
        freqs[s] += 1

    for j in jewels:
        count += freqs[j]

    return count


jewels = "aA"
stones = "aAAbbbb"
print(numJewelsInStones(jewels, stones))