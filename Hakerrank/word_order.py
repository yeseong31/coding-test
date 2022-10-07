from collections import defaultdict, deque

n = int(input())
dic = defaultdict(int)

strs = deque()

for _ in range(n):
    s = input()
    dic[s] += 1

print(len(dic))
for d in dic:
    print(dic[d], end=' ')
