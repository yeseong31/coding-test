# 가장 흔한 단어(151p)

# 금지된 단어를 제외한 가장 흔한 단어
# 대소문자, 구두점 무시
import re
from collections import Counter


def mostCommonWord(paragraph: str, banned: list[str]) -> str:
    words = [x for x in re.sub(r'[^\w]', ' ', paragraph).lower().split() if x not in banned]
    return Counter(words).most_common(1)[0][0]


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(mostCommonWord(paragraph, banned))
# "ball"

paragraph = "a."
banned = []
print(mostCommonWord(paragraph, banned))
# "a"
