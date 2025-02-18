import collections

for _ in range(int(input())):
    dic = collections.defaultdict(int)
    n = int(input())
    for _ in range(n):
        _, kind = map(str, input().split())
        dic[kind] += 1

    result = 1
    for i in dic.values():
        result *= (i + 1)
    print(result - 1)
