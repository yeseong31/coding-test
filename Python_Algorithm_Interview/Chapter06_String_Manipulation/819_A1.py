# 풀이 1 - 리스트 컴프리헨션, Counter 객체 사용
import collections
import re


def mostCommonWord(paragraph: str, banned: list[str]) -> str:
    words = [x for x in re.sub(r'[^\w]', ' ', paragraph).lower().split() if x not in banned]
    counts = collections.defaultdict(int)
    for word in words:
        counts[word] += 1
    return max(counts, key=counts.get)
