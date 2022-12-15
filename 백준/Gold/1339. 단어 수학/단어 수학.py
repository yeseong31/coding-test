from collections import defaultdict

n = int(input())
words = []
weights = defaultdict(int)
dic = defaultdict(str)

for _ in range(n):
    target = input()
    words.append(target)
    for i in range(len(target) - 1, -1, -1):
        weights[target[i]] += 10 ** (len(target) - i)

weights = sorted(weights.items(), key=lambda x: x[1], reverse=True)
cnt = 9
for i, j in weights:
    dic[i] = str(cnt)
    cnt -= 1

print(sum(int(''.join(dic[x] for x in alphabet)) for alphabet in words))
