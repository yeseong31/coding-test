import collections

for _ in range(int(input())):
    dic = collections.defaultdict(int)
    # 의상의 수
    n = int(input())
    for _ in range(n):
        # 의상의 이름과 종류
        _, kind = map(str, input().split())
        dic[kind] += 1

    result = 1
    for i in dic.values():
        result *= (i + 1)
    print(result - 1)
