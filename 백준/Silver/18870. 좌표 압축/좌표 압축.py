import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

dic = {v: i for i, v in enumerate(sorted(list(set(data))))}

for d in data:
    print(dic[d], end=' ')