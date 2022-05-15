# 풀이 4 - 파이썬다운 방식

def numJewelsInStones(jewels: str, stones: str) -> int:
    return sum(s in jewels for s in stones)
