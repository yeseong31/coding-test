import collections
import re


def mostCommonWord(paragraph: str, banned: list[str]) -> str:
    words = [x for x in re.sub(r'[^\w]', ' ', paragraph).lower().split() if x not in banned]
    cnt = collections.Counter(words)
    return cnt.most_common(1)[0][0]
