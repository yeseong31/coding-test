# 풀이 1 - 해시 테이블을 이용한 풀이

def numJewelsInStones(jewels: str, stones: str) -> int:
    freqs = {}
    count = 0

    for s in stones:
        if s not in freqs:
            freqs[s] = 1
        else:
            freqs[s] += 1

    for j in jewels:
        if j in freqs:
            count += freqs[j]

    return count


jewels = "aA"
stones = "aAAbbbb"
print(numJewelsInStones(jewels, stones))