# 풀이 3 - Counter로 계산 생략
from collections import Counter


def numJewelsInStones(jewels: str, stones: str) -> int:
    freqs = Counter(stones)     # Counter는 존재하지 않는 키의 경우 0을 출력하므로 예외 처리가 필요 없음
    count = 0

    for j in jewels:
        count += freqs[j]

    return count


jewels = "aA"
stones = "aAAbbbb"
print(numJewelsInStones(jewels, stones))