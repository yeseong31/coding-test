# 보석과 돌(298p)
from collections import defaultdict


def numJewelsInStones(jewels: str, stones: str) -> int:
    dic = defaultdict(int)
    for s in stones:
        dic[s] += 1

    cnt = 0
    for j in jewels:
        cnt += dic[j]

    return cnt


jewels = "aA"
stones = "aAAbbbb"
print(numJewelsInStones(jewels, stones))
