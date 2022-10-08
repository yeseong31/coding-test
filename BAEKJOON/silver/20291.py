import sys

from collections import defaultdict

n = int(sys.stdin.readline())
dic = defaultdict(int)

for _ in range(n):
    dic[input().split('.')[1]] += 1

for d in sorted(dic):
    print(f'{d} {dic[d]}')
