import sys
from collections import defaultdict

input = sys.stdin.readline
n = int(input().strip())
words = [input().strip() for _ in range(n)]

weights = defaultdict(int)
for word in words:
    for i in range(len(word) - 1, -1, -1):
        weights[word[i]] += 10 ** (len(word) - i)

cnt = 9
dic = defaultdict(str)
for i, j in sorted(weights.items(), key=lambda x: x[1], reverse=True):
    dic[i] = str(cnt)
    cnt -= 1

print(sum(int(''.join(dic[x] for x in word)) for word in words))
